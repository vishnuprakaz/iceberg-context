import json,sys,re,collections,csv
D=sys.argv[1]; r=json.load(open(f'{D}/raw/reviewers.json'))
def area(t):
    m=re.match(r'^(?:Revert ")?([^:]{1,40}):',t)
    if not m: return '(none)'
    a=m.group(1).strip().split(',')[0].strip(); a=re.sub(r'\s*\d[\d.x]*$','',a).lower()
    return {'kafka-connect':'kafka connect','openapi':'rest/openapi','rest':'rest/openapi','rest spec':'rest/openapi','open-api':'rest/openapi','specification':'spec','infra':'build/infra','build':'build/infra','ci':'build/infra','site':'docs','website':'docs','doc':'docs'}.get(a,a)
rows=[]
for repo,v in r.items():
    print('=====',repo)
    byarea=collections.defaultdict(collections.Counter)
    for login,x in sorted(v.items(),key=lambda kv:-kv[1]['n']):
        if x['n']==0: continue
        allp=len(x['prs']); x['prs']=[(n,t) for n,t in x['prs'] if not re.match(r'^(Build: |build\(deps\): |chore\(deps\): )?[Bb]ump ',t)]; x['n_nonbot']=len(x['prs']) if allp else x['n']
        ac=collections.Counter(area(t) for _,t in x['prs'])
        for a,n in ac.items(): byarea[a][login]+=n
        print(f"{login:20s} {x['asf']:22s} {x['n']:4d} {x['n_nonbot']:4d} "+', '.join(f'{a}:{n}' for a,n in ac.most_common(5)))
        rows.append([repo,login,x['asf'],x['n'],x['n_nonbot']]+[ '; '.join(f'{a}:{n}' for a,n in ac.most_common(8))])
    if repo=='apache/iceberg':
        print('--- per area top reviewers (PRs created since 2026-05-13, excl. own)')
        for a,c in sorted(byarea.items(),key=lambda kv:-sum(kv[1].values())):
            if sum(c.values())<15: continue
            print(f'{a:15s}',', '.join(f'{l}({n})' for l,n in c.most_common(6)))
with open(f'{D}/raw/reviewers_summary.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['repo','login','asf_id_or_tag','reviewed_prs_6m','reviewed_nonbot_6m','areas']); w.writerows(rows)
