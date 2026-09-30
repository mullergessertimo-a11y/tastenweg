import sys, json; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import kern
from fingering import finger_hand
from fractions import Fraction as F
def build(fn, handof, until_bar=None):
    ev, bars, _ = kern.parse(fn)
    if until_bar: ev = [e for e in ev if e[0] < bars[until_bar+1]] if until_bar+1 in bars else ev
    # Griffe mit mehr als 5 Tönen in einer Hand: obere Töne an die rechte, untere an die linke Hand abgeben
    from collections import defaultdict
    hand = {id(e): handof(e) for e in ev}
    byt = defaultdict(list)
    for e in ev: byt[(e[0], hand[id(e)])].append(e)
    for (t, h), grp in byt.items():
        if len(grp) > 5:
            grp.sort(key=lambda e: e[2])
            extra = grp[5:] if h == 'L' else grp[:-5]
            for e in extra: hand[id(e)] = 'R' if h == 'L' else 'L'
    out = []
    for h in 'LR':
        hs = [e for e in ev if hand[id(e)] == h]
        fs = finger_hand([[float(e[0]), float(e[1]), e[2]] for e in hs], left=(h=='L'))
        for e, f in zip(hs, fs): out.append([e[0], e[1], e[2], h, f, e[4]])
    out.sort(key=lambda e: (e[0], e[2]))
    bt = [float(bars[k]) for k in sorted(bars)]
    return out, bt
def fmt(x): 
    x = float(x); s = f"{x:.4f}".rstrip('0').rstrip('.'); return s
def enc(out): return ";".join(f"{fmt(t)},{fmt(d)},{sp},{h},{f}" for t,d,m,h,f,sp in out)
pieces = {
 'bach': build('wtc1p01.krn', lambda e: 'R' if e[3]=='0aa' else 'L'),
 'chopin4': build('chopin28-04.krn', lambda e: 'L' if e[3].startswith('0') else 'R'),
 'nocturne': build('noct09-2.krn', lambda e: 'L' if e[3].startswith('0') else 'R'),
 'moonfull': build('moon1.krn', lambda e: 'R' if (e[3].startswith('1') or abs(float(e[1]) - 1/3) < 1e-3) else 'L'),
}
res = {}
for k,(out,bt) in pieces.items():
    zeros = sum(1 for e in out if e[4]==0)
    print(k, 'Töne', len(out), 'ohne Finger', zeros, 'Takte', len(bt), 'Länge', float(max(e[0]+e[1] for e in out)))
    res[k] = {'events': enc(out), 'bars': bt}
json.dump(res, open('gen.json','w'))
print('Größe', sum(len(v['events']) for v in res.values()))
