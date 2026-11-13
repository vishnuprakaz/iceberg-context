import json, sys, re
def clean(path):
    d = json.load(open(path))
    words = []
    lines = []  # (start_ms, text) per event
    for ev in d.get('events', []):
        segs = ev.get('segs')
        if not segs: continue
        t = ''.join(s.get('utf8', '') for s in segs)
        if t.strip() == '': continue
        lines.append((ev.get('tStartMs', 0), t.replace('\n', ' ')))
    text = ' '.join(t for _, t in lines)
    text = re.sub(r'\s+', ' ', text).strip()
    return lines, text
if __name__ == '__main__':
    for p in sys.argv[1:]:
        lines, text = clean(p)
        dur = lines[-1][0] / 3600000 if lines else 0
        w = len(text.split())
        print(p.split('/')[-1], 'events', len(lines), 'words', w, 'hours', round(dur, 2), 'wph', round(w / dur) if dur else 0,
              'has>>', text.count('>>'), 'periods', text.count('. '), 'brackets', len(re.findall(r'\[[a-z ]+\]', text)))
