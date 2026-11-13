import json, sys, re
sys.path.insert(0, sys.argv[0].rsplit('/', 1)[0])
from clean_json3 import clean
src, info, out = sys.argv[1:4]
meta = json.load(open(info))
lines, _ = clean(src)
paras, cur, start = [], [], 0
for ms, t in lines:
    for i, piece in enumerate(re.split(r'\s*>>\s*', t)):
        if i > 0 and cur:  # speaker change marker from YouTube ASR
            paras.append((start, ' '.join(cur))); cur = []; start = ms
        if not cur: start = ms
        if piece.strip(): cur.append(piece.strip())
    if cur and ms - start > 90000 and cur[-1].endswith(('.', '?', '!')):
        paras.append((start, ' '.join(cur))); cur = []
if cur: paras.append((start, ' '.join(cur)))
def ts(ms):
    s = ms // 1000; return '%d:%02d:%02d' % (s // 3600, s // 60 % 60, s % 60)
vid = meta['id']
body = '\n\n'.join('[%s](https://youtu.be/%s?t=%d) %s' % (ts(ms), vid, ms // 1000, re.sub(r'\s+', ' ', p)) for ms, p in paras)
words = sum(len(p.split()) for _, p in paras)
hdr = f"""---
type: Meeting Transcript
title: "{meta['title'].strip()}"
video_id: {vid}
resource: https://www.youtube.com/watch?v={vid}
upload_date: {meta['upload_date'][:4]}-{meta['upload_date'][4:6]}-{meta['upload_date'][6:]}
duration_s: {meta['duration']}
caption_track: en-orig (YouTube ASR, auto-generated)
words: {words}
---

# {meta['title'].strip()}

Description: {meta.get('description','').strip()}

## Transcript

"""
open(out, 'w').write(hdr + body + '\n')
print(out, len(paras), 'paragraphs', words, 'words')
