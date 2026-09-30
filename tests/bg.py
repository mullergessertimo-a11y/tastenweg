import numpy as np, sys, json
from scipy.signal import butter, lfilter, sosfilt
sr=48000
def bp(x,f,q):
    b,a=butter(2,[max(20,f/(1+1/(2*q))),min(sr/2-100,f*(1+1/(2*q)))],btype='band',fs=sr); return lfilter(b,a,x)
FORM={'a':(800,1200,2500),'e':(400,2000,2600),'i':(300,2300,3000),'o':(450,800,2800),'u':(325,700,2500)}
def speech(dur, rng, f0base):
    out=np.zeros(int(sr*dur)); t=0.0
    while t<dur-0.4:
        sl=rng.uniform(0.12,0.35); n=int(sl*sr); st=int(t*sr)
        # F0-Verlauf: Gleiten + Jitter
        f0=f0base*np.exp(np.linspace(0,rng.uniform(-0.25,0.25),n))*(1+0.01*rng.standard_normal(n).cumsum()/np.sqrt(n))
        ph=np.cumsum(f0/sr); src=(ph%1.0)*2-1   # Sägezahn ~ Stimmlippen
        src=src-np.convolve(src,np.ones(8)/8,'same')*0.5
        v=rng.choice(list(FORM)); y=sum(bp(src,f,6)*g for f,g in zip(FORM[v],(1,0.5,0.25)))
        env=np.sin(np.linspace(0,np.pi,n))**0.6
        if rng.random()<0.3: y=y+rng.standard_normal(n)*0.3*np.exp(-np.linspace(0,6,n))  # Frikativ
        out[st:st+n]+=y*env; t+=sl+rng.uniform(0.02,0.25)
    return out/ (np.abs(out).max()+1e-9)
def clap(rng):
    n=int(0.12*sr); return rng.standard_normal(n)*np.exp(-np.arange(n)/(0.012*sr))
def typing(dur,rng):
    out=np.zeros(int(sr*dur))
    for t in np.cumsum(rng.uniform(0.08,0.25,int(dur*6))):
        if t>dur-0.05: break
        n=int(0.03*sr); c=bp(rng.standard_normal(n),rng.uniform(2000,4000),3)*np.exp(-np.arange(n)/(0.004*sr))
        out[int(t*sr):int(t*sr)+n]+=c
    return out
def knock(rng):
    n=int(0.25*sr); f=rng.uniform(80,160); t=np.arange(n)/sr
    return (np.sin(2*np.pi*f*t)*np.exp(-t/0.04)+0.3*rng.standard_normal(n)*np.exp(-t/0.01))
def clink(rng):
    n=int(0.8*sr); t=np.arange(n)/sr; f=rng.uniform(2200,3500)
    return (np.sin(2*np.pi*f*t)+0.4*np.sin(2*np.pi*f*2.71*t))*np.exp(-t/0.25)
def whistle(dur,rng,steady):
    n=int(dur*sr); f=np.full(n,rng.uniform(900,1400)) if steady else 1000*np.exp(np.cumsum(rng.standard_normal(n))*0.0004)
    f=f*(1+0.004*np.sin(2*np.pi*5*np.arange(n)/sr))   # Vibrato
    env=np.minimum(1,np.minimum(np.arange(n),n-np.arange(n))/(0.05*sr))
    return np.sin(2*np.pi*np.cumsum(f)/sr)*env
def fan(dur,rng):
    n=int(dur*sr); x=bp(rng.standard_normal(n),300,0.7)*0.6+0.4*np.sin(2*np.pi*97*np.arange(n)/sr)
    return x
def place(out,x,t,g):
    st=int(t*sr); L=min(len(x),len(out)-st); out[st:st+L]+=x[:L]*g
def make_bg(total,rng,level=1.0):
    out=np.zeros(int(sr*total)); t=2.0
    events=['speech_m','speech_f','clap','typing','knock','clink','whistle_g','whistle_s','fan','speech_m','clap','knock']
    rng.shuffle(events); log=[]
    for e in events:
        if t>total-2: break
        if e.startswith('speech'): d=rng.uniform(2,3.5); place(out,speech(d,rng,110 if e=='speech_m' else 210),t,0.25*level)
        elif e=='clap': d=0.6; [place(out,clap(rng),t+i*0.3,0.5*level) for i in range(2)]
        elif e=='typing': d=2.0; place(out,typing(d,rng),t,0.35*level)
        elif e=='knock': d=0.8; [place(out,knock(rng),t+i*0.2,0.6*level) for i in range(3)]
        elif e=='clink': d=0.9; place(out,clink(rng),t,0.15*level)
        elif e=='whistle_g': d=1.5; place(out,whistle(d,rng,False),t,0.12*level)
        elif e=='whistle_s': d=1.2; place(out,whistle(d,rng,True),t,0.12*level)
        elif e=='fan': d=3.0; place(out,fan(d,rng),t,0.08*level)
        log.append((round(t,1),e)); t+=d+rng.uniform(0.4,0.9)
    return out,log
if __name__=='__main__':
    spec=json.loads(sys.argv[1]); rng=np.random.default_rng(spec.get('seed',1))
    import mk  # noqa
