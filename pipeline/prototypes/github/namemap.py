import json,re,sys,collections
D=sys.argv[1]
d=json.load(open(f'{D}/raw/search_prs_issues.json'))
out={}
for repo,fn in [('apache/iceberg','iceberg'),('apache/iceberg-python','iceberg-python')]:
    bynum={p['number']:p['user'] for p in d[repo]['prs']}
    m=collections.defaultdict(collections.Counter)
    for line in open(f'{D}/raw/gitlog-{fn}.txt',errors='replace'):
        if not line.startswith('@@'): continue
        h,an,cn,ad,cd,s=line[2:].rstrip('\n').split('\x1f',5)
        mm=re.search(r'\(#(\d+)\)\s*$',s)
        if mm and int(mm.group(1)) in bynum: m[an][bynum[int(mm.group(1))]]+=1
    out[repo]={a:c.most_common(1)[0][0] for a,c in m.items()}
json.dump(out,open(f'{D}/raw/name_to_login.json','w'),indent=0)
logins=set(json.load(open(f'{D}/raw/committer_logins.json')).values())
allmapped=set(out['apache/iceberg'].values())|set(out['apache/iceberg-python'].values())
print('mapped',len(out['apache/iceberg']),len(out['apache/iceberg-python']))
print('committer logins seen as PR authors:',sorted(logins&allmapped))
print('not seen:',sorted(logins-allmapped))
for n in ['Ryan Blue','Eduard Tudenhoefner','Drew Gallardo','geruh','Yuya Ebihara','Huaxin Gao','Steven Zhen Wu','Szehon Ho','Russell Spitzer','Amogh Jahagirdar','Prashant Singh','Kevin Liu','Alex Stephen','Gang Wu','Sung Yun','Matthew Topol','Bryan Keller','Piotr Findeisen','Shawn Chang','GuoYu','Manu Zhang','Hongyue/Steve Zhang','Anoop Johnson','Neelesh Salian','Vova Kolmakov','Talat UYARER','Xin Huang','Eunbin Son','Uros Bojanic','Swapna Marru','Anurag Mantripragada','Yufei Gu','Jack Ye','Daniel Weeks','Anton Okolnychyi','pvary','Maximilian Michels','gaborkaszab','Fokko Driesprong','Anas Khan','Xander','Rahul Shivu Mahadev','JB Onofré','Joy Haldar','Thomas Powell','Alexandre Dutra']:
    print(n,'->',out['apache/iceberg'].get(n),out['apache/iceberg-python'].get(n))
