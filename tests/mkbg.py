import sys, json, numpy as np
sys.argv=[sys.argv[0]]+sys.argv[1:]
import mk, bg
spec=json.loads(sys.argv[1]); rng=np.random.default_rng(spec.get('seed',1))
sr=48000
if spec.get('seq'):
    t=spec.get('lead',2.0); ev=[]
    for grp in spec['seq']: ev.append((t,grp)); t+=spec.get('gap',0.8)
    x=mk.render(ev,t+4,spec.get('pedal',False),rng)
else:
    x=np.zeros(int(sr*spec['dur']))
b,log=bg.make_bg(len(x)/sr,rng,spec.get('bglevel',1.0))
x=x+b[:len(x)]*spec.get('bgmix',1.0)
mk.write(spec['out'],mk.laptop_mic(x,rng)); print(spec['out'],log)
