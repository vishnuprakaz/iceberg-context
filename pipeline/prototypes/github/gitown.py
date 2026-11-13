import sys, json, collections, re
path, repo, out = sys.argv[1], sys.argv[2], sys.argv[3]
commits=[]; cur=None
for line in open(path, encoding='utf-8', errors='replace'):
    line=line.rstrip('\n')
    if line.startswith('@@'):
        h,an,cn,ad,cd,s=line[2:].split('\x1f',5)
        cur=dict(h=h,an=an,cn=cn,ad=ad,cd=cd,s=s,files=[]); commits.append(cur)
    elif line and cur: cur['files'].append(line)
def mod(f):
    p=f.split('/')
    if repo=='iceberg':
        if p[0] in ('spark','flink','hive','mr','hive3','hive-runtime','delta-lake','kafka-connect','aws','azure','gcp','dell','aliyun','nessie','snowflake','bigquery','open-api','format','docs','site','api','core','data','parquet','orc','arrow','common','bundled-guava','aws-bundle','gcp-bundle','azure-bundle','.github','dev','gradle','pig','python','jmh','examples','baseline','build-logic','mr'): 
            if p[0] in ('aws-bundle',): return 'aws'
            if p[0] in ('gcp-bundle',): return 'gcp'
            if p[0] in ('azure-bundle',): return 'azure'
            if p[0] in ('hive3','hive-runtime','mr','hive'): return 'hive/mr'
            if p[0] in ('gradle','build-logic','baseline','dev'): return 'build'
            return p[0]
        if len(p)==1: return 'root/build'
        return p[0]
    else:
        if p[0]=='pyiceberg':
            if len(p)>2: return 'pyiceberg/'+p[1]
            return 'pyiceberg/'+p[1].replace('.py','')
        if p[0] in ('tests',): return 'tests/'+(p[1] if len(p)>2 else '')
        if p[0]=='mkdocs': return 'docs'
        return p[0] if len(p)>1 else 'root/build'
stats=collections.defaultdict(lambda:{'all':collections.Counter(),'12m':collections.Counter(),'first':None,'n12':0,'nall':0})
monthly=collections.Counter(); committers=collections.Counter(); authors12=collections.Counter(); authors_all=collections.Counter()
first_commit={}
for c in reversed(commits):
    first_commit.setdefault(c['an'],c['ad'][:10])
for c in commits:
    recent=c['ad']>='2025-11-13'
    committers[c['cn']]+=1
    authors_all[c['an']]+=1
    if recent: authors12[c['an']]+=1; monthly[c['ad'][:7]]+=1
    ms=set()
    for f in c['files']:
        m=mod(f)
        if repo=='iceberg-python' and m.startswith('tests/'): continue
        ms.add(m)
    for m in ms:
        s=stats[m]; s['all'][c['an']]+=1; s['nall']+=1
        if recent: s['12m'][c['an']]+=1; s['n12']+=1
res={'total_commits':len(commits),'commits_12m':sum(authors12.values()),'committer_field':committers.most_common(10),
 'authors_12m_count':len(authors12),'top_authors_12m':authors12.most_common(25),'top_authors_all':authors_all.most_common(25),
 'monthly_12m':sorted(monthly.items()),
 'new_authors_12m':sum(1 for a,d in first_commit.items() if d>='2025-11-13'),
 'modules':{m:{'n_all':s['nall'],'n_12m':s['n12'],'top_all':s['all'].most_common(8),'top_12m':s['12m'].most_common(8)} for m,s in sorted(stats.items(), key=lambda x:-x[1]['nall'])}}
json.dump(res,open(out,'w'),indent=1)
print(json.dumps({k:v for k,v in res.items() if k!='modules'},indent=0)[:3000])
for m,v in res['modules'].items():
    if v['n_all']<40: continue
    print(f"## {m} all={v['n_all']} 12m={v['n_12m']}\n  ALL: "+', '.join(f'{a}({n})' for a,n in v['top_all'][:6])+"\n  12M: "+', '.join(f'{a}({n})' for a,n in v['top_12m'][:6]))
