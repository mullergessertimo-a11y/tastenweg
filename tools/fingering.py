"""Automatischer Fingersatz (dynamische Programmierung, Kostenmodell nach Parncutt et al. 1997).
Eingabe: Ereignisse einer Hand [t, d, midi]; Ausgabe: Finger je Ereignis."""
from itertools import combinations
BLACK = {1,3,6,8,10}
# (MinPrac, MinComf, MinRel, MaxRel, MaxComf, MaxPrac) für rechte Hand, Fingerpaar (i<j), Abstand = Tonhöhe(j) - Tonhöhe(i)
T = {(1,2):(-5,-3,1,5,8,10),(1,3):(-4,-2,3,7,10,12),(1,4):(-3,-1,5,9,12,14),(1,5):(-1,1,7,10,13,15),
     (2,3):(1,1,1,2,3,5),(2,4):(1,1,3,4,5,7),(2,5):(2,2,5,6,8,10),(3,4):(1,1,1,2,2,4),(3,5):(1,1,3,4,5,7),(4,5):(1,1,1,2,3,5)}
def pair_cost(fa, pa, fb, pb, chord=False):
    if fa == fb:
        return 0.0 if pa == pb else (50.0 if chord else 6.0 + 0.5*abs(pa-pb))
    if fa > fb: fa, pa, fb, pb = fb, pb, fa, pa
    mnP, mnC, mnR, mxR, mxC, mxP = T[(fa, fb)]
    d = pb - pa; c = 0.0
    if d < mnC: c += 2*(mnC - d)
    if d > mxC: c += 2*(d - mxC)
    if d < mnR: c += (mnR - d)
    if d > mxR: c += (d - mxR)
    if d < mnP or d > mxP: c += 10 if not chord else 40
    return c * (1.5 if chord else 1.0)
def key_cost(f, midi):
    b = (midi % 12) in BLACK
    return (1.0 if (b and f == 1) else 0) + (0.5 if (b and f == 5) else 0)
def assign(new, held, free):
    """alle Fingerzuordnungen für neue Töne, sodass alle klingenden Töne (tief->hoch) aufsteigende Finger haben"""
    res = []
    for combo in combinations(sorted(free), len(new)):
        cand = list(held) + list(zip(new, combo))
        s = sorted(cand)
        if all(s[i][1] < s[i+1][1] for i in range(len(s)-1)): res.append(tuple(zip(new, combo)))
    return res
def finger_hand(events, left=False, beam=150):
    """events: Liste von [t, d, midi]; gibt Finger (Liste gleicher Länge) zurück."""
    if not events: return []
    sgn = -1 if left else 1                       # linke Hand gespiegelt wie rechte behandeln
    idx = sorted(range(len(events)), key=lambda i: (events[i][0], events[i][2]))
    groups = []
    for i in idx:
        t = events[i][0]
        if groups and abs(groups[-1][0] - t) < 1e-6: groups[-1][1].append(i)
        else: groups.append([t, [i]])
    # Zustand: (klingende Töne ((pitch, finger), ...), zuletzt angeschlagene ((pitch, finger), ...), Ende der Töne)
    states = {((), ()): (0.0, None, {})}         # key -> (kosten, vorgänger-key, zuordnung idx->finger) (Pfad über back-pointer)
    history = []
    for gi, (t, members) in enumerate(groups):
        new = sorted(members, key=lambda i: sgn*events[i][2])
        newp = [sgn*events[i][2] for i in new]
        nxt = {}
        for key, (cost, _, _) in states.items():
            sounding, last = key
            # noch klingende Töne (gehaltene Töne dieser Hand) behalten ihren Finger
            held = [(p, f) for (p, f, end) in sounding if end > t + 1e-6]
            if len(held) + len(new) > 5: held = []
            free = set(range(1, 6)) - {f for _, f in held}
            opts = assign(newp, held, free) if len(new) <= 5 else []
            if not opts and held:
                held = []; opts = assign(newp, [], set(range(1,6)))
                cost += 3.0                      # gehaltene Töne umgreifen/loslassen
            if not opts:                          # mehr als 5 Töne: nur die äußeren 5
                continue
            prev_end = max([e for (_, _, e) in sounding], default=t)
            gap = max(0.0, t - prev_end)
            w = 1.0 / (1.0 + 2*gap)               # nach Pausen darf die Hand neu ansetzen
            for opt in opts:
                c = cost
                fing = [f for _, f in opt]
                # Griff: alle gleichzeitig klingenden Töne
                allk = held + list(opt)
                for (pa, fa), (pb, fb) in combinations(allk, 2): c += pair_cost(fa, pa, fb, pb, chord=True)
                # Übergang vom zuletzt angeschlagenen Griff
                if last:
                    s = 0.0
                    for (pa, fa) in last:
                        for (pb, fb) in opt: s += pair_cost(fa, pa, fb, pb)
                    c += w * s / (len(last) * len(opt))
                for (p, f) in opt: c += key_cost(f, sgn*p)
                ends = [(p, f, t + events[i][1]) for (p, f), i in zip(opt, new)]
                snd = tuple(sorted([(p, f, e) for (p, f, e) in sounding if e > t + 1e-6 and (p, f) in held] + ends))
                nk = (snd, tuple(opt))
                if nk not in nxt or c < nxt[nk][0]: nxt[nk] = (c, key, dict(zip(new, fing)))
        if not nxt:                               # Notfall: Zustand zurücksetzen
            nxt = {((), ()): (min(v[0] for v in states.values()), next(iter(states)), {i: 0 for i in new})}
        best = sorted(nxt.items(), key=lambda kv: kv[1][0])[:beam]
        states = dict(best); history.append(states)
    # Rückverfolgung
    out = [0]*len(events)
    key = min(states, key=lambda k: states[k][0])
    for gi in range(len(history)-1, -1, -1):
        c, prev, amap = history[gi][key]
        for i, f in amap.items(): out[i] = f
        key = prev
    return out
