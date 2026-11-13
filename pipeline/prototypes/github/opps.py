import sys, json, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs
out=sys.argv[1]; res={}
for repo in ['apache/iceberg','apache/iceberg-python']:
    r={}
    def items(q,sort=None,n=30):
        d=gs.call(f'repo:{repo} {q}',per_page=n,sort=sort,order='desc' if sort else None)
        return d['total_count'],[gs.slim(i) for i in d['items']]
    r['good_first_issue']=items('is:issue is:open label:"good first issue"')
    r['help_wanted']=items('is:issue is:open label:"help wanted"')
    r['top_thumbs_no_pr']=items('is:issue is:open -linked:pr',sort='reactions-+1')
    r['top_thumbs_all']=items('is:issue is:open',sort='reactions-+1',n=15)
    r['recent_bugs']=items('is:issue is:open label:bug created:>=2026-10-13',sort='created')
    r['recent_bugs_kind']=items('is:issue is:open label:kind:bug created:>=2026-10-13',sort='created')
    r['recent_issues_unlabeled_nopr']=items('is:issue is:open -linked:pr created:>=2026-10-13',sort='created')
    r['proposals_open']=items('is:issue is:open label:proposal',sort='updated')
    r['pr_review_none_nondraft']=items('is:pr is:open -is:draft review:none',sort='created')
    r['pr_review_none_ge14d']=items('is:pr is:open -is:draft review:none created:<=2026-10-30')
    r['pr_review_required_ge14d']=items('is:pr is:open -is:draft review:required created:<=2026-10-30')
    r['pr_approved_open']=items('is:pr is:open -is:draft review:approved',sort='updated')
    r['pr_changes_requested_open']=gs.count(f'repo:{repo} is:pr is:open review:changes_requested')
    r['issues_open_no_pr']=gs.count(f'repo:{repo} is:issue is:open -linked:pr')
    res[repo]=r; print(repo,'done',flush=True)
sib={}
months=[('2026-05-01','2026-05-31'),('2026-06-01','2026-06-30'),('2026-07-01','2026-07-31'),('2026-08-01','2026-08-31'),('2026-09-01','2026-09-30'),('2026-10-01','2026-10-31')]
for repo in ['apache/iceberg-rust','apache/iceberg-go','apache/iceberg-cpp']:
    s={'open_prs':gs.count(f'repo:{repo} is:pr is:open'),'open_issues':gs.count(f'repo:{repo} is:issue is:open'),
       'good_first_issue':gs.count(f'repo:{repo} is:issue is:open label:"good first issue"'),
       'merged_per_month':{a[:7]:gs.count(f'repo:{repo} is:pr merged:{a}..{b}') for a,b in months}}
    it=gs.fetch_all(f'repo:{repo} is:pr is:merged','2026-05-13','2026-11-13',field='merged')
    s['top_merged_authors_6m']=collections.Counter(i['user']['login'] for i in it).most_common(12)
    s['merged_6m']=len(it)
    sib[repo]=s; print(repo,s,flush=True)
res['siblings']=sib
json.dump(res,open(out,'w'),indent=1)
