import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs
out=sys.argv[1]
res={}
for repo in ['apache/iceberg','apache/iceberg-python']:
    prs=gs.fetch_all(f'repo:{repo} is:pr','2025-11-01','2026-11-13')
    openold=gs.fetch_all(f'repo:{repo} is:pr is:open','2018-01-01','2025-10-31')
    issues=gs.fetch_all(f'repo:{repo} is:issue','2025-11-01','2026-11-13')
    openissues=gs.fetch_all(f'repo:{repo} is:issue is:open','2017-01-01','2025-10-31')
    res[repo]=dict(prs=[gs.slim(i) for i in prs],open_prs_old=[gs.slim(i) for i in openold],
                   issues=[gs.slim(i) for i in issues],open_issues_old=[gs.slim(i) for i in openissues])
    print(repo,{k:len(v) for k,v in res[repo].items()},flush=True)
json.dump(res,open(out,'w'))
