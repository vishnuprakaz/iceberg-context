import json,collections,sys,re
D=sys.argv[1]
M=json.load(open(D+'/messages_norm.json')); R=json.load(open(D+'/thread_index.json'))
M12=[m for m in M if m['date']>='2025-11-13']
c=collections.Counter(m['name'] for m in M12)
print('distinct senders 12mo',len(c)); print('TOP SENDERS'); print(c.most_common(30))
R12=[x for x in R if x['start']>='2025-11-13' and not x['orphan']]
st=collections.defaultdict(collections.Counter)
for x in R12:
    k='DISCUSS' if x['type'] in('discuss/proposal','discuss-release') and '[DISC' in x['subject'].upper() else ('VOTE' if x['type'].startswith('vote') else None)
    if k: st[k][x['starter']]+=1
for k in st: print(k,'starters',sum(st[k].values()),st[k].most_common(20))
# replies-only
starters=collections.Counter(x['starter'] for x in R12)
print('REPLY-HEAVY (msgs, threads started)'); print([(n,v,starters.get(n,0)) for n,v in c.most_common(30)])
print('RELEASES 12mo')
for x in R:
    if x['start']>='2025-11-01' and x['type'] in('vote-release','announce-release') : print(x['start'],x['type'][:8],x['replies'],x['starter'],'|',x['subject'][:80])
