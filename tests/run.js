const { chromium } = require('playwright');
const [,, wav, piece, calib, secs, hand] = process.argv;
(async()=>{
 const b = await chromium.launch({args:['--use-fake-ui-for-media-stream','--use-fake-device-for-media-stream','--use-file-for-fake-audio-capture='+__dirname+'/'+wav+'%noloop','--autoplay-policy=no-user-gesture-required']});
 const p = await b.newPage({viewport:{width:1300,height:1000}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.addInitScript(c=>{ window.__cfg = c; }, JSON.parse(process.env.CFG||'{}')); await p.goto((process.env.TW_URL || 'http://localhost:8765/index.html')+'#'+piece);
 await p.evaluate(()=>{ try{localStorage.clear()}catch(e){} });
 await p.reload(); await p.waitForTimeout(300);
 if(hand) await p.click(`#handSeg button[data-hand="${hand}"]`);
 await p.click('#playBtn'); await p.click('#playBtn'); // audio + samples laden
 await p.waitForTimeout(2500);
 if(calib==='1') await p.click('#calBtn'); else await p.click('#micTop');
 const t0=Date.now(); let last='';
 while(Date.now()-t0 < (+secs)*1000){
   await p.waitForTimeout(250);
   const st = await p.$eval('#stats', e=>e.textContent.match(/Richtig (\d+)Falsch (\d+)/).slice(1).join('/'));
   const cal = await p.$eval('#calCard', e=>e.hidden?'':document.getElementById('calProg').textContent+' '+document.getElementById('calMsg').textContent);
   const line = `${st} ${await p.$eval('#nowBar',e=>e.textContent)} ${cal}`;
   if(line!==last){ console.log(((Date.now()-t0)/1000).toFixed(1), line, '|', await p.$eval('#micHeard',e=>e.textContent)); last=line; }
 }
 console.log('ERR', errs); await b.close();
})();
