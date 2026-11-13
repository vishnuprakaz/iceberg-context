import json, re, collections, csv, sys
D=sys.argv[1]
M=json.load(open(D+'/messages.json'))
def nm(n):
    n=re.sub(r'\s+via\s+.*$','',n).strip().strip("'\"")
    if ',' in n and len(n.split(','))==2: a,b=n.split(','); n=f"{b.strip()} {a.strip()}"
    return n
for m in M: m['name']=nm(m['name'])
T=collections.defaultdict(list)
for m in M: T[m['root']].append(m)
def classify(s, body, gdoc):
    s0=re.sub(r'^((re|fwd?|aw)\s*:\s*)+','',s,flags=re.I); u=s0.upper()
    lang='java'
    for k,pat in [('pyiceberg',r'PYICEBERG|\[PYTHON\]'),('rust',r'RUST'),('go',r'\bGO\b|\[GO\]'),('cpp',r'C\+\+|ICEBERG-CPP|\[CPP\]'),('terraform','TERRAFORM')]:
        if re.search(pat,u): lang=k; break
    if '[RESULT]' in u: t='result'
    elif '[VOTE]' in u or u.startswith('VOTE'):
        t='vote-release' if re.search(r'RELEASE|\bRC\d|RC\d',u) else ('vote-committer' if re.search(r'COMMITTER|PMC',u) else 'vote-spec/process')
    elif re.search(r'\[ANNOUNCE\]',u) and re.search(r'RELEASE|ICEBERG\s+\S*\s*\d+\.\d+|PYICEBERG\s+\d',u) and not re.search(r'MEETUP|SUMMIT|LAKEHOUSE|CFP',u): t='announce-release'
    elif re.search(r'NEW COMMITTER|NEW PMC|PMC MEMB',u): t='announce-people'
    elif re.search(r'MEETUP|SUMMIT|LAKEHOUSE DAY|OSA CON|CONFLUENCE 20|REGISTER|CFP',u): t='events/community'
    elif re.search(r'SYNC|INVITATION:|MEETING',u): t='sync-meeting'
    elif re.search(r'CONFLUENT|SUBSCRIB|SLACK|MAILING LIST|UFFHG|SWAG|SECURITY CONTACT',u) or len(u)<6: t='admin/noise'
    elif re.search(r'REVIEW|PR\s*#|\bPR\b|PULL REQUEST',u) and not '[DISCUSS' in u: t='review-request'
    elif re.search(r'\[DISCUSS',u) and re.search(r'RELEASE|\d+\.\d+(\.\d+)?\b.*(RELEASE|PATCH)|PATCH RELEASE',u): t='discuss-release'
    elif re.search(r'\[DISCUSS|PROPOSAL|\[REPORT\]|PSA',u) or gdoc: t='discuss/proposal'
    elif re.search(r'\[QUESTION\]|\?$',u): t='question'
    else: t='general'
    return t, lang
rows=[]
for r,ms in T.items():
    ms.sort(key=lambda m:m['date']); f=ms[0]
    t,lang=classify(f['subject'],f['body'],any(m['gdoc'] for m in ms))
    rows.append(dict(root=r,start=f['date'][:10],last=ms[-1]['date'][:10],subject=f['subject'],starter=f['name'],
      replies=len(ms)-1,participants=len({m['name'] for m in ms}),type=t,lang=lang,gdoc=any(m['gdoc'] for m in ms),
      orphan=bool(re.match(r'^(re|fwd?)\s*:',f['subject'],re.I)),
      url='https://lists.apache.org/thread/'+'' ,first_body=f['body'][:600]))
rows.sort(key=lambda x:x['start'])
json.dump(rows,open(D+'/thread_index.json','w'),indent=1,ensure_ascii=False)
with open(D+'/thread_index.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=[k for k in rows[0] if k!='first_body']); w.writeheader()
    for x in rows: w.writerow({k:v for k,v in x.items() if k!='first_body'})
json.dump(M,open(D+'/messages_norm.json','w'))
six=[x for x in rows if x['start']>='2026-05-13' and not x['orphan']]
print('6mo threads',len(six)); c=collections.Counter(x['type'] for x in six)
for k,v in c.most_common(): print(f'  {k:22} {v:4}  msgs={sum(x["replies"]+1 for x in six if x["type"]==k)}')
print('gdoc-linked threads',sum(x['gdoc'] for x in six))
