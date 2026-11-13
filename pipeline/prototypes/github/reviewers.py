import sys, json, os, collections, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs
logins=json.load(open(sys.argv[1])); out=sys.argv[2]
res={}
for repo,since in [('apache/iceberg','2026-05-13'),('apache/iceberg-python','2026-05-13')]:
    res[repo]={}
    for asf,login in logins.items():
        q=f'repo:{repo} is:pr reviewed-by:{login} -author:{login}'
        n=gs.count(f'{q} created:>={since}')
        nums=[]
        if n and repo=='apache/iceberg' or n>=5:
            items=gs.fetch_all(q,since,'2026-11-13')
            nums=[(i['number'],i['title']) for i in items]
        res[repo][login]=dict(asf=asf,n=n,prs=nums)
        print(repo,login,n,flush=True)
json.dump(res,open(out,'w'))
