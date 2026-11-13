import mailbox, email, email.utils, email.header, json, re, sys, glob, os, csv
from email.policy import default
D=sys.argv[1]
def dh(s):
    if s is None: return ''
    try: return str(email.header.make_header(email.header.decode_header(str(s))))
    except Exception: return str(s)
def body(m):
    try:
        if m.is_multipart():
            for p in m.walk():
                if p.get_content_type()=='text/plain':
                    return p.get_payload(decode=True).decode(p.get_content_charset() or 'utf-8','replace')
            return ''
        return m.get_payload(decode=True).decode(m.get_content_charset() or 'utf-8','replace')
    except Exception: return ''
msgs={}
for f in sorted(glob.glob(D+'/mbox/*.mbox')):
    for m in mailbox.mbox(f):
        mid=(m.get('Message-ID') or '').strip()
        if not mid or mid in msgs: continue
        name,addr=email.utils.parseaddr(dh(m.get('From')))
        name=re.sub(r'\s*\(.*?\)\s*$','',name).strip().strip('"') or addr.split('@')[0]
        try: dt=email.utils.parsedate_to_datetime(m.get('Date')).astimezone(__import__('datetime').timezone.utc)
        except Exception: continue
        refs=(m.get('References') or '').split()
        irt=(m.get('In-Reply-To') or '').strip()
        b=body(m)
        # strip quoted
        own='\n'.join(l for l in b.splitlines() if not l.startswith('>'))
        msgs[mid]=dict(mid=mid,name=name,date=dt.isoformat(),month=dt.strftime('%Y-%m'),subject=' '.join(dh(m.get('Subject')).split()),
            irt=irt,refs=refs,body=own[:4000],gdoc=bool(re.search(r'docs\.google\.com',own)),month_file=os.path.basename(f))
# threading: root = first ref present, else irt, else self; fallback normalized subject
def norm(s): return re.sub(r'^((re|fwd?|aw)\s*:\s*)+','',s.strip(),flags=re.I).lower()
subjroot={}
for mid,m in sorted(msgs.items(),key=lambda x:x[1]['date']):
    root=None
    for r in m['refs']+[m['irt']]:
        if r in msgs: root=msgs[r].get('root',r); break
    if root is None:
        ns=norm(m['subject'])
        if re.match(r'^(re|fwd?)\s*:',m['subject'],re.I) and ns in subjroot: root=subjroot[ns]
        else: root=mid
    m['root']=root
    subjroot.setdefault(norm(m['subject']),root)
json.dump(list(msgs.values()),open(D+'/messages.json','w'))
print(len(msgs))
