// Misst Fehlerkennungen: alle Töne des Stücks werden als Kandidaten geprüft (Debug-Modus)
const { chromium } = require('playwright');
const [,, wav, piece, secs] = process.argv;
(async()=>{
 const b = await chromium.launch({args:['--use-fake-ui-for-media-stream','--use-fake-device-for-media-stream','--use-file-for-fake-audio-capture='+__dirname+'/'+wav+'%noloop','--autoplay-policy=no-user-gesture-required']});
 const p = await b.newPage({viewport:{width:1300,height:1000}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.addInitScript(c=>{ window.__cfg = c; }, JSON.parse(process.env.CFG||'{}')); await p.goto((process.env.TW_URL || 'http://localhost:8765/index.html')+'#'+piece); await p.waitForTimeout(300);
 await p.evaluate(()=>{ window.__debugMic='all'; });
 await p.click('#playBtn'); await p.click('#playBtn'); await p.waitForTimeout(2500);
 await p.click('#micTop'); const t0=Date.now(); const seen=new Map(); let heardFrames=0, frames=0; const heardNotes={};
 while(Date.now()-t0 < (+secs)*1000){
   await p.waitForTimeout(100); frames++;
   const d = await p.evaluate(()=>window.__micdbg);
   const h = await p.$eval('#micHeard',e=>e.textContent.replace('Ich höre: ','').trim());
   if(h){ heardFrames++; h.split(/\s+/).forEach(n=>heardNotes[n]=(heardNotes[n]||0)+1); }
   if(d) for(const o of d.on){ const k=o[0]+'@'+o[1]; if(!seen.has(k)) seen.set(k, ((Date.now()-t0)/1000).toFixed(1)); }
 }
 const st = await p.$eval('#stats', e=>e.textContent.match(/Richtig (\d+)/)[1]);
 console.log(`${wav} ${piece}: Onsets=${seen.size} Richtig=${st} ICH-HOERE=${(100*heardFrames/frames).toFixed(0)}%`, [...seen].map(([k,t])=>t+':'+k.split('@')[0]).join(' '), JSON.stringify(heardNotes), errs.join(';'));
 await b.close();
})();
