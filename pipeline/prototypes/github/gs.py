"""Rate-limited GitHub search helper with on-disk cache."""
import subprocess, json, time, hashlib, os, datetime as dt
CACHE=os.environ.get('GSCACHE')
_last=[0.0]
def call(q, page=1, per_page=100, sort=None, order=None, kind='issues'):
    key=hashlib.sha1(json.dumps([kind,q,page,per_page,sort,order]).encode()).hexdigest()
    cp=os.path.join(CACHE,key+'.json')
    if os.path.exists(cp): return json.load(open(cp))
    for attempt in range(6):
        wait=2.2-(time.time()-_last[0])
        if wait>0: time.sleep(wait)
        _last[0]=time.time()
        args=['gh','api','-X','GET',f'search/{kind}','-f',f'q={q}','-f',f'per_page={per_page}','-f',f'page={page}']
        if sort: args+=['-f',f'sort={sort}']
        if order: args+=['-f',f'order={order}']
        r=subprocess.run(args,capture_output=True,text=True)
        if r.returncode==0:
            d=json.loads(r.stdout); json.dump(d,open(cp,'w')); return d
        err=r.stderr+r.stdout
        if 'rate limit' in err.lower() or '403' in err or '429' in err:
            time.sleep(30*(attempt+1)); continue
        raise RuntimeError(err[:500])
    raise RuntimeError('rate-limited repeatedly: '+q)
def count(q): return call(q,per_page=1)['total_count']
def fetch_all(q, start, end, field='created'):
    """Fetch all items for q in [start,end] dates, slicing when >1000."""
    d=call(f'{q} {field}:{start}..{end}',per_page=1)
    n=d['total_count']
    if n>1000 and start!=end:
        s=dt.date.fromisoformat(start); e=dt.date.fromisoformat(end); m=s+(e-s)/2
        return fetch_all(q,start,m.isoformat(),field)+fetch_all(q,(m+dt.timedelta(days=1)).isoformat(),end,field)
    items=[]; page=1
    while len(items)<min(n,1000):
        r=call(f'{q} {field}:{start}..{end}',page=page)
        if not r['items']: break
        items+=r['items']; page+=1
    return items
def slim(i):
    return dict(number=i['number'],title=i['title'],user=i['user']['login'],assoc=i.get('author_association'),
        state=i['state'],created=i['created_at'],closed=i['closed_at'],updated=i['updated_at'],
        merged=(i.get('pull_request') or {}).get('merged_at'),draft=i.get('draft'),
        labels=[l['name'] for l in i['labels']],comments=i['comments'],
        thumbs=(i.get('reactions') or {}).get('+1',0),reactions=(i.get('reactions') or {}).get('total_count',0),
        assignees=[a['login'] for a in i.get('assignees') or []],url=i['html_url'],
        is_pr='pull_request' in i)
