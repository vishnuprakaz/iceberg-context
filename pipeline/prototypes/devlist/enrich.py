import json,glob,csv,sys,re,collections
D=sys.argv[1]
mp={}
for f in glob.glob(D+'/stats/*.json'):
    for e in json.load(open(f))['emails']: mp[e['message-id'].strip()]=e['mid']
R=json.load(open(D+'/thread_index.json')); M=json.load(open(D+'/messages_norm.json'))
T=collections.defaultdict(list)
for m in M: T[m['root']].append(m)
for x in R:
    x['url']='https://lists.apache.org/thread/'+mp[x['root']] if x['root'] in mp else ''
    ms=T[x['root']]; txt=' '.join(m['body'] for m in ms)
    x['plus1']=len({m['name'] for m in ms if re.search(r'(^|\n)\s*\+1\b',m['body'])}) if x['type'].startswith('vote') else ''
    x['has_result']=bool(any('[RESULT]' in m['subject'].upper() or re.search(r'vote (passes|has passed|passed)',m['body'],re.I) for m in ms))
json.dump(R,open(D+'/thread_index.json','w'),indent=1,ensure_ascii=False)
with open(D+'/thread_index.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=[k for k in R[0] if k!='first_body']); w.writeheader()
    for x in R: w.writerow({k:v for k,v in x.items() if k!='first_body'})
print('with url',sum(1 for x in R if x['url']),len(R))
# monthly table 12 mo
mc=collections.Counter(m['month'] for m in M); nt=collections.Counter(x['start'][:7] for x in R if not x['orphan'])
act=collections.defaultdict(set); snd=collections.defaultdict(set)
for m in M: act[m['month']].add(m['root']); snd[m['month']].add(m['name'])
for k in sorted(mc):
    if k>='2025-11': print(k,mc[k],nt[k],len(act[k]),len(snd[k]))
for x in R:
    if x['start']>='2026-08-13' and x['type']=='vote-spec/process': print(x['start'],x['replies'],x['plus1'],x['has_result'],x['subject'][:70],x['url'])
