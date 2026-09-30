import os
import subprocess, numpy as np, wave, sys, json
from scipy.signal import butter, lfilter, fftconvolve
sr=48000
NCAL=0
cache={}
def load(n):
    if n not in cache:
        raw=subprocess.run(['ffmpeg','-loglevel','error','-i',os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'samples', f'{n}.mp3'),'-f','f32le','-ac','1','-ar',str(sr),'-'],capture_output=True).stdout
        cache[n]=np.frombuffer(raw,dtype=np.float32).copy()
    return cache[n]
NAMES=["C","Cs","D","Ds","E","F","Fs","G","Gs","A","As","B"]
def nm(m): return NAMES[m%12]+str(m//12-1)
def render(events, total, pedal=False, rng=None, changes=None):
    out=np.zeros(int(sr*total))
    ch_times=[events[i][0] for i in (changes or [])]
    for ei,(t,notes) in enumerate(events):
        for m in notes:
            x=load(nm(m)).copy()
            if not pedal or ei < NCAL:
                d=int(0.7*sr); env=np.ones(len(x)); env[d:]=np.exp(-np.arange(len(x)-d)/(0.08*sr)); x*=env
            elif ch_times:
                nxt=[c for c in ch_times if c>t+1e-6]
                if nxt:
                    d=int((nxt[0]-t)*sr)
                    if d<len(x): env=np.ones(len(x)); env[d:]=np.exp(-np.arange(len(x)-d)/(0.08*sr)); x*=env
            vel=rng.uniform(0.5,1.0)
            st=int(sr*t); L=min(len(x),len(out)-st); out[st:st+L]+=x[:L]*0.25*vel
    return out
def laptop_mic(x, rng):
    b,a=butter(2,180/(sr/2),'high'); x=lfilter(b,a,x)          # schwacher Bass
    b,a=butter(1,7000/(sr/2),'low'); x=lfilter(b,a,x)
    # Raumhall
    L=int(0.5*sr); ir=rng.standard_normal(L)*np.exp(-np.arange(L)/(0.09*sr))*0.25; ir[0]=1
    x=fftconvolve(x,ir)[:len(x)]
    # Rauschen (rosa-ish) + Lüfter-Brummen
    n=np.cumsum(rng.standard_normal(len(x))); n=n-np.convolve(n,np.ones(2000)/2000,'same'); n/=np.abs(n).max()
    t=np.arange(len(x))/sr
    x=x+0.004*n+0.002*np.sin(2*np.pi*120*t)+0.0015*rng.standard_normal(len(x))
    return x*rng.uniform(0.3,1.0)
def write(fn,x):
    x=x/max(1,np.abs(x).max()*1.05)
    w=wave.open(fn,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
if __name__=='__main__':
    spec=json.loads(sys.argv[1]); rng=np.random.default_rng(spec.get('seed',1))
    t=spec.get('lead',2.0); ev=[]
    for c in spec.get('calib',[]):
        ev.append((t,[c])); t+=1.7
    if spec.get('calib'): t+=1.5
    for grp in spec['seq']:
        ev.append((t,grp)); t+=spec.get('gap',0.8)
    nc=len(spec.get('calib',[])); NCAL=nc; x=render(ev,t+4,spec.get('pedal',False),rng,[c+nc for c in spec.get('changes',[])])
    write(spec['out'],laptop_mic(x,rng))
    print(spec['out'], round(t,1),'s', 'perf starts at', ev[len(spec.get('calib',[]))][0])
