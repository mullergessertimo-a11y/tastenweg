"""Schlanker Humdrum-**kern-Leser: liefert Ereignisse [t, d, midi, spalte, schreibweise], Taktanfänge."""
import re
from fractions import Fraction as F
PC = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
def dur_of(tok):
    m = re.search(r'(\d+)%(\d+)', tok)
    if m: return F(4)*F(int(m.group(2)), int(m.group(1)))
    m = re.search(r'(\d+)(\.*)', tok)
    if not m: return None
    n = int(m.group(1)); base = F(8) if n == 0 else F(4, n)
    d = base; add = base
    for _ in m.group(2): add /= 2; d += add
    return d
def pitch_of(tok):
    m = re.search(r'([a-gA-G])\1*', tok)
    if not m: return None
    letters = m.group(0); L = letters[0]
    octv = 3 + len(letters) if L.islower() else 4 - len(letters)
    rest = tok[m.end():]
    acc = 0; sp = ''
    a = re.match(r'(##|#|--|-|n)?', rest).group(1) or ''
    acc = {'##':2,'#':1,'--':-2,'-':-1,'n':0,'':0}[a]
    sp = {'##':'##','#':'#','--':'bb','-':'b'}.get(a, '')
    midi = 12*(octv+1) + PC[L.lower()] + acc
    return midi, f"{L.upper()}{sp}{octv}"
def parse(fn):
    cols = []           # je Spalte: dict(kern, id)
    T = F(0); events = []; bars = {}; pending_ties = {}
    busy = {}
    for line in open(fn, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('!'): continue
        toks = line.split('\t')
        if line.startswith('**'):
            cols = [{'kern': t == '**kern', 'id': str(i)} for i, t in enumerate(toks)]; continue
        if line.startswith('*'):
            new = []; i = 0
            while i < len(toks):
                t = toks[i]; c = cols[i]
                if t == '*^': new += [dict(c, id=c['id']+'a'), dict(c, id=c['id']+'b')]
                elif t == '*v':
                    j = i
                    while j+1 < len(toks) and toks[j+1] == '*v': j += 1
                    new.append(dict(c, id=c['id'][:-1] if len(c['id'])>1 else c['id'])); i = j
                elif t == '*-': pass
                else: new.append(c)
                i += 1
            cols = new; continue
        if line.startswith('='):
            m = re.match(r'=(\d+)', toks[0])
            if m and int(m.group(1)) not in bars: bars[int(m.group(1))] = T
            continue
        # Datenzeile
        for i, t in enumerate(toks):
            if i >= len(cols) or not cols[i]['kern'] or t == '.': continue
            ds = []
            for sub in t.split(' '):
                if 'q' in sub.lower() or 'yy' in sub: continue
                d = dur_of(sub)
                if d is None: continue
                ds.append(d)
                if 'r' in sub: continue
                pm = pitch_of(sub)
                if not pm: continue
                midi, sp = pm; cid = cols[i]['id']
                key = (cid, midi)
                if ('_' in sub or ']' in sub) and key in pending_ties:
                    pending_ties[key][1] += d
                    if ']' in sub: del pending_ties[key]
                    continue
                ev = [T, d, midi, cid, sp]; events.append(ev)
                if '[' in sub: pending_ties[key] = ev
            if ds: busy[i] = T + max(ds)
        nxt = [b for b in busy.values() if b > T]
        T = min(nxt) if nxt else T
    return events, bars, cols
