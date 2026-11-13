import json,sys,collections,statistics as st,datetime as dt,re,csv
D=sys.argv[1]; d=json.load(open(f'{D}/raw/search_prs_issues.json'))
NOW=dt.datetime(2026,11,13,tzinfo=dt.timezone.utc)
P=lambda s: dt.datetime.fromisoformat(s.replace('Z','+00:00')) if s else None
out={}
def area(t):
    m=re.match(r'^(?:Revert ")?([^:]{1,40}):',t)
    if not m: return '(none)'
    a=m.group(1).strip().split(',')[0].strip()
    a=re.sub(r'\s*\d[\d.x]*$','',a)  # Spark 4.0 -> Spark
    return a.lower()
for repo,v in d.items():
    prs=[p for p in v['prs'] if p['created']>='2025-11-13']
    allopen=[p for p in v['prs']+v['open_prs_old'] if p['state']=='open']
    allopen={p['number']:p for p in allopen}.values()
    r={}
    r['prs_opened_12m']=len(prs)
    r['merged_12m']=sum(1 for p in prs if p['merged'])
    r['closed_unmerged_12m']=sum(1 for p in prs if p['state']=='closed' and not p['merged'])
    bots=('dependabot[bot]','github-actions[bot]','renovate[bot]')
    human=[p for p in prs if p['user'] not in bots]
    r['human_prs_12m']=len(human); r['dependabot_prs_12m']=len(prs)-len(human)
    ttm=[(P(p['merged'])-P(p['created'])).total_seconds()/86400 for p in human if p['merged']]
    r['median_days_to_merge_human']=round(st.median(ttm),2); q=st.quantiles(ttm,n=4); r['ttm_p25_p75']=[round(q[0],2),round(q[2],2)]
    r['p90_days_to_merge']=round(st.quantiles(ttm,n=10)[8],1)
    r['merge_rate_human_closed']=round(sum(1 for p in human if p['merged'])/max(1,sum(1 for p in human if p['state']=='closed')),3)
    ac=collections.Counter(p['assoc'] for p in human); r['author_association_12m']=dict(ac)
    r['first_time_share']=round((ac.get('FIRST_TIME_CONTRIBUTOR',0)+ac.get('FIRST_TIMER',0))/len(human),3)
    r['unique_authors_12m']=len({p['user'] for p in human})
    mo=collections.defaultdict(lambda:[0,0])
    for p in v['prs']:
        mo[p['created'][:7]][0]+=1
    for p in v['prs']+v['open_prs_old']:
        if p['merged']: mo[p['merged'][:7]][1]+=1
    r['monthly_opened_merged']={k:mo[k] for k in sorted(mo)}
    ages=[(NOW-P(p['created'])).days for p in allopen]
    r['open_prs']=len(ages); r['open_drafts']=sum(1 for p in allopen if p['draft'])
    b=collections.Counter()
    for a in ages: b['<7d' if a<7 else '7-30d' if a<30 else '30-90d' if a<90 else '90-365d' if a<365 else '>1y']+=1
    r['open_age_buckets']=dict(b)
    idle=[(NOW-P(p['updated'])).days for p in allopen]
    r['open_idle_gt30d']=sum(1 for x in idle if x>30); r['open_labeled_stale']=sum(1 for p in allopen if 'stale' in p['labels'])
    r['stale_closed_12m']=sum(1 for p in prs if p['state']=='closed' and not p['merged'] and 'stale' in p['labels'])
    lab=collections.Counter(l for p in prs for l in p['labels']); r['top_labels_prs_12m']=lab.most_common(20)
    ar=collections.Counter(area(p['title']) for p in human); r['title_areas_12m']=ar.most_common(25)
    ao=collections.Counter(area(p['title']) for p in allopen if p['user'] not in bots); r['open_by_area']=ao.most_common(15)
    au=collections.Counter(p['user'] for p in human if p['merged']); r['top_merged_authors_12m']=au.most_common(20)
    # open nonDraft, waiting: created>14d, comments<=1
    wait=[p for p in allopen if not p['draft'] and p['user'] not in bots and (NOW-P(p['created'])).days>=14 and p['comments']<=1 and 'stale' not in p['labels']]
    r['open_nondraft_ge14d_le1comment']=len(wait)
    r['examples_waiting']=[(p['url'],p['title'],p['created'][:10],p['comments']) for p in sorted(wait,key=lambda p:p['created'])[:12]]
    iss=v['issues']+v['open_issues_old']
    openi={i['number']:i for i in iss if i['state']=='open'}.values()
    r['open_issues']=len(openi); r['issues_opened_12m']=sum(1 for i in v['issues'] if i['created']>='2025-11-13')
    il=collections.Counter(l for i in openi for l in i['labels']); r['open_issue_labels']=il.most_common(20)
    out[repo]=r
    with open(f'{D}/raw/prs_{repo.split("/")[1]}.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['number','title','user','assoc','state','draft','created','merged','closed','updated','comments','labels','area'])
        for p in v['prs']+v['open_prs_old']: w.writerow([p['number'],p['title'],p['user'],p['assoc'],p['state'],p['draft'],p['created'],p['merged'],p['closed'],p['updated'],p['comments'],'|'.join(p['labels']),area(p['title'])])
json.dump(out,open(f'{D}/raw/pr_stats.json','w'),indent=1)
for repo,r in out.items():
    print('=====',repo)
    for k,v in r.items(): print(k,':',v)
