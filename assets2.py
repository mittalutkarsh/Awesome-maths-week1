CSS = r"""
:root{
  --ink:#11242b; --ink-soft:#4a626c; --paper:#eef2f3; --card:#ffffff;
  --rule:#d3dcdf; --teal:#0d6b6e; --teal-dark:#094f52; --gold:#b1820f; --gold-soft:#fff5dd;
  --ok:#146b47; --ok-soft:#e6f4ec; --no:#a32c1e; --no-soft:#fbeae7;
  --term:#0e1f23; --term-ink:#d8e6e6; --term-dim:#7f9a9b;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
  --ui:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;
}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;font-family:var(--ui);font-size:16px;line-height:1.55;color:var(--ink);
  background:var(--paper);display:flex;flex-direction:column;overflow:hidden}
button{font-family:inherit;cursor:pointer}
:focus-visible{outline:3px solid var(--teal);outline-offset:2px}

/* ---------------- top bar ---------------- */
.top{display:flex;align-items:center;gap:12px;padding:9px 14px;background:var(--card);
  border-bottom:1px solid var(--rule);flex:0 0 auto;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:9px;font-weight:700;letter-spacing:-.01em;min-width:0}
.brand .mark{width:28px;height:28px;border-radius:6px;background:var(--teal);color:#fff;
  display:grid;place-items:center;font-family:var(--mono);font-size:15px}
.brand small{display:block;font-weight:400;font-size:12.5px;color:var(--ink-soft);letter-spacing:0;white-space:nowrap}
.top .nav{display:flex;gap:6px}
.iconbtn{width:34px;height:34px;border:1px solid var(--rule);background:#fff;border-radius:6px;
  color:var(--ink);font-size:15px;line-height:1;display:grid;place-items:center}
.iconbtn:hover{background:#f2f7f7}
.iconbtn:disabled{opacity:.4;cursor:not-allowed}
select.picker{font-family:inherit;font-size:15px;padding:7px 10px;border:1px solid var(--rule);
  border-radius:6px;background:#fff;color:var(--ink);max-width:min(46vw,420px)}
.top .spacer{flex:1}
.stat{font-family:var(--mono);font-size:13px;color:var(--ink-soft);white-space:nowrap;padding-left:10px}
a.stat{color:var(--teal-dark)}
.stat b{color:var(--ink)}
.navtoggle{display:none}

/* ---------------- shell ---------------- */
.shell{flex:1;min-height:0;display:grid;
  grid-template-columns:230px minmax(320px,1fr) minmax(340px,1.05fr)}
.pane{min-height:0;overflow:auto;background:var(--card);border-right:1px solid var(--rule)}
.right{min-height:0;display:flex;flex-direction:column;background:var(--card)}

/* ---------------- sidebar ---------------- */
.side{background:#f7fafa}
.side h3{margin:0;padding:12px 14px 6px;font-size:12.5px;font-weight:700;color:var(--ink-soft)}
.side ol{list-style:none;margin:0 0 10px;padding:0}
.side li button{width:100%;text-align:left;background:none;border:0;border-left:3px solid transparent;
  padding:7px 12px 7px 11px;font-size:14.5px;color:var(--ink);display:flex;gap:8px;align-items:baseline}
.side li button:hover{background:#eef4f4}
.side li button.on{background:#e3eeee;border-left-color:var(--teal);font-weight:700}
.side .dot{font-family:var(--mono);font-size:12px;color:var(--ink-soft);flex:0 0 14px}
.side .dot.done{color:var(--ok)} .side .dot.part{color:var(--gold)}

/* ---------------- description pane ---------------- */
.tabs{display:flex;gap:2px;border-bottom:1px solid var(--rule);padding:0 10px;
  position:sticky;top:0;background:var(--card);z-index:3}
.tabs button{background:none;border:0;border-bottom:2px solid transparent;padding:11px 12px 9px;
  font-size:14.5px;color:var(--ink-soft)}
.tabs button.on{color:var(--ink);border-bottom-color:var(--teal);font-weight:700}
.desc{padding:18px 22px 46px}
.desc h1{font-family:Fraunces,Georgia,serif;font-size:23px;line-height:1.2;margin:0 0 10px}
.desc h2{font-family:Fraunces,Georgia,serif;font-size:20px;margin:26px 0 6px}
.desc h3{font-size:16.5px;margin:20px 0 4px}
.desc .tag{display:inline-block;font-family:var(--mono);font-size:11.5px;color:var(--teal-dark);
  border-bottom:2px solid var(--gold);padding-bottom:2px;margin:0 0 10px;letter-spacing:.04em}
.dimtext{color:var(--ink-soft);font-size:14.5px}
.desc ol,.desc ul{padding-left:20px;margin:0 0 12px}
.desc li{margin:4px 0}
.desc p,.desc li{max-width:62ch}
.desc p{margin:0 0 12px}
.chips{display:flex;gap:7px;flex-wrap:wrap;margin:0 0 14px}
.chip{font-size:12.5px;padding:3px 9px;border-radius:99px;border:1px solid var(--rule);color:var(--ink-soft)}
.chip.hard{background:var(--no-soft);border-color:#eccac4;color:var(--no)}
.chip.core{background:var(--gold-soft);border-color:#eedcae;color:#8a6408}
.chip.set{background:#e9f2f2;border-color:#cfe0e0;color:var(--teal-dark)}
.qbody{font-size:17px}
.m{font-family:var(--mono);font-size:.93em;background:#f1f6f6;border:1px solid #e0e9e9;
  border-radius:4px;padding:1px 5px;white-space:nowrap}
.stack{background:#f7fafa;border:1px solid #e3ebeb;border-radius:4px;padding:11px 13px;
  font-family:var(--mono);font-size:14px;line-height:1.75;white-space:pre-wrap;overflow-x:auto;margin:12px 0}
.rulebox{border-left:4px solid var(--gold);background:var(--gold-soft);padding:11px 14px;margin:14px 0;border-radius:0 4px 4px 0}
.rulebox p:last-child{margin:0}
table.cmp{border-collapse:collapse;width:100%;font-size:14.5px;margin:13px 0}
table.cmp th,table.cmp td{border:1px solid var(--rule);padding:7px 9px;text-align:left}
table.cmp th{background:#f1f6f6}
.desc .two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:1500px){.desc .two{grid-template-columns:1fr}}
.steplist{list-style:none;padding:0;margin:8px 0 0}
.steplist li{padding:7px 0;border-top:1px dashed var(--rule);font-size:15px;display:flex;gap:9px}
.steplist .ic{font-family:var(--mono);flex:0 0 16px}
.steplist .ic.ok{color:var(--ok)} .steplist .ic.giv{color:var(--gold)}

/* ---------------- work pane ---------------- */
.worktop{flex:0 0 auto;border-bottom:1px solid var(--rule);background:#fbfdfd}
.steptabs{display:flex;gap:6px;overflow-x:auto;padding:9px 12px}
.steptabs button{flex:0 0 auto;font-family:var(--mono);font-size:12.5px;padding:5px 10px;border-radius:99px;
  border:1px solid var(--rule);background:#fff;color:var(--ink-soft)}
.steptabs button.on{border-color:var(--teal);background:#e3eeee;color:var(--teal-dark);font-weight:500}
.steptabs button.done{border-color:#bcdcc9;background:var(--ok-soft);color:var(--ok)}
.steptabs button.giv{border-color:#eedcae;background:var(--gold-soft);color:#8a6408}
.prompt{padding:0 16px 13px;font-size:16.5px}
.prompt .lab{font-family:var(--mono);font-size:12px;color:var(--ink-soft);display:block;margin-bottom:3px}
.editwrap{flex:1 1 auto;min-height:130px;display:flex;background:#fcfdfd;border-bottom:1px solid var(--rule);overflow:hidden}
.gutter{flex:0 0 42px;padding:10px 6px 10px 0;text-align:right;font-family:var(--mono);font-size:13.5px;
  line-height:1.62;color:#9db0b3;background:#f4f8f8;border-right:1px solid var(--rule);overflow:hidden;white-space:pre}
.editwrap textarea{flex:1;border:0;resize:none;padding:10px 12px;font-family:var(--mono);font-size:14.5px;
  line-height:1.62;background:transparent;color:var(--ink);outline:none}
.answerbar{flex:0 0 auto;padding:11px 14px;display:flex;gap:9px;align-items:center;flex-wrap:wrap;background:#fff}
.answerbar label{font-family:var(--mono);font-size:12.5px;color:var(--ink-soft)}
.answerbar input{flex:1 1 150px;min-width:0;font-family:var(--mono);font-size:15px;padding:9px 11px;
  border:1px solid var(--rule);border-radius:6px;background:#fcfdfd;color:var(--ink)}
.btn{font-size:15px;padding:9px 15px;border-radius:6px;border:1px solid var(--teal);background:var(--teal);color:#fff;
  display:inline-flex;gap:7px;align-items:center}
.btn:hover:not(:disabled){background:var(--teal-dark);border-color:var(--teal-dark)}
.btn.ghost{background:#fff;color:var(--teal-dark)}
.btn.ghost:hover:not(:disabled){background:#eef5f5;color:var(--teal-dark)}
.btn:disabled{opacity:.45;cursor:not-allowed}
.btn small{font-family:var(--mono);font-size:11px;opacity:.8}
.actionbar{flex:0 0 auto;padding:0 14px 12px;display:flex;gap:9px;align-items:center;flex-wrap:wrap;background:#fff}
.tries{font-family:var(--mono);font-size:12.5px;color:var(--ink-soft);margin-left:auto}
.tries i{font-style:normal;color:var(--no)}

.btn.hintbtn{border-color:#e0c684;background:var(--gold-soft);color:#7d5a06}
.btn.hintbtn:hover:not(:disabled){background:#fbeec9;border-color:#d4b877;color:#5f4404}

/* ---------------- hint dialog ---------------- */
.mask{position:fixed;inset:0;background:rgba(14,31,35,.55);display:none;z-index:50;
  align-items:center;justify-content:center;padding:20px}
.mask.open{display:flex}
.modal{background:var(--card);border-radius:10px;max-width:520px;width:100%;
  box-shadow:0 18px 50px rgba(8,26,30,.35);overflow:hidden}
.modal header{display:flex;align-items:center;gap:10px;padding:13px 16px;background:var(--gold-soft);
  border-bottom:1px solid #eedcae}
.modal header b{font-family:Fraunces,Georgia,serif;font-size:17px}
.modal header span{font-family:var(--mono);font-size:12px;color:#8a6408}
.modal header button{margin-left:auto;background:none;border:0;font-size:20px;line-height:1;color:#8a6408}
.modal .body{padding:16px 18px;font-size:16.5px}
.modal .body .q{font-size:14.5px;color:var(--ink-soft);margin:0 0 10px}
.modal .body p{margin:0 0 12px}
.modal footer{padding:0 18px 16px;display:flex;gap:9px;align-items:center}
.modal footer .note{font-size:13.5px;color:var(--ink-soft)}

/* ---------------- console ---------------- */
.term{flex:1 1 44%;min-height:150px;background:var(--term);color:var(--term-ink);display:flex;flex-direction:column}
.term .bar{flex:0 0 auto;display:flex;align-items:center;gap:8px;padding:8px 13px;
  border-bottom:1px solid #1d3439;font-family:var(--mono);font-size:12px;color:var(--term-dim)}
.term .bar b{color:#e7f1f1;font-weight:500;letter-spacing:.04em}
.term .bar button{margin-left:auto;background:none;border:1px solid #27454a;color:var(--term-dim);
  border-radius:5px;font-family:var(--mono);font-size:11.5px;padding:3px 8px}
.term .bar button:hover{color:#e7f1f1}
.log{flex:1;overflow:auto;padding:12px 14px 20px;font-family:var(--mono);font-size:13.5px;line-height:1.66}
.log .e{margin:0 0 11px;white-space:pre-wrap;word-break:break-word}
.log .cmd{color:#8fd6cf}
.log .good{color:#7fd4a2}
.log .bad{color:#f2a99c}
.log .hint{color:#f0cd82}
.log .give{color:#a8cfe6}
.log .dim{color:var(--term-dim)}
.log .head{color:#e7f1f1;border-bottom:1px solid #1d3439;padding-bottom:6px}
.log b{color:#fff;font-weight:500}
.log .ans{display:block;margin-top:5px;padding:8px 10px;background:#152c31;border-left:3px solid var(--gold);
  color:#f7e9c6;border-radius:0 4px 4px 0}
.log .empty{color:var(--term-dim)}

/* ---------------- responsive ---------------- */
@media(max-width:1080px){
  body{overflow:auto}
  .shell{grid-template-columns:1fr;grid-auto-rows:min-content}
  .pane,.right{border-right:0;border-bottom:1px solid var(--rule);overflow:visible}
  .side{display:none}
  .side.open{display:block}
  .navtoggle{display:grid}
  .editwrap{min-height:170px}
  .term{min-height:240px}
  .log{max-height:none}
  .tabs{position:static}
}
"""

JS_CHECK = r"""
/* ============ math + answer checking ============ */
const SUP = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4','\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9'};
function deSup(s){
  let out='', run='';
  for(const ch of String(s)){
    if(SUP[ch]){ run += SUP[ch]; }
    else { if(run){ out += '^'+run; run=''; } out += ch; }
  }
  if(run) out += '^'+run;
  return out;
}
function norm(s){ return deSup(s).toLowerCase().replace(/,/g,'').replace(/\s+/g,' ').trim(); }
function isPrime(n){ if(n<2) return false; for(let d=2;d*d<=n;d++) if(n%d===0) return false; return true; }
function numsIn(s){ return (norm(s).match(/\d+(?:\.\d+)?/g)||[]).map(Number); }
function parseFactor(str){
  let s = deSup(str).toLowerCase();
  if(s.indexOf('=')>=0) s = s.split('=').pop();
  s = s.replace(/[\u00d7\u22c5\u00b7\u2219\u2715\u2022]/g,'*').replace(/\bx\b/g,'*')
       .replace(/\*\*/g,'^').replace(/\s+/g,'').replace(/[()]/g,'');
  if(!s) return null;
  const toks = s.split('*').filter(t=>t.length);
  if(!toks.length) return null;
  const map={};
  for(const t of toks){
    const m=t.match(/^(\d+)(?:\^(\d+))?$/);
    if(!m) return null;
    const b=parseInt(m[1],10), e=m[2]?parseInt(m[2],10):1;
    if(b===1) continue;
    if(b<1) return null;
    map[b]=(map[b]||0)+e;
  }
  return map;
}
function mapValue(m){ let v=1; for(const b in m) v*=Math.pow(+b,m[b]); return v; }
function sameMap(a,b){ const ka=Object.keys(a),kb=Object.keys(b);
  return ka.length===kb.length && ka.every(k=>a[k]===b[k]); }
function allPrimeBases(m){ return Object.keys(m).every(b=>isPrime(+b)); }

function checkAnswer(step, raw){
  const v = norm(raw);
  if(!v) return {ok:false, note:'Nothing in the answer box yet.'};
  if(step.type==='factor'){
    const want=parseFactor(step.answer), got=parseFactor(raw);
    if(!got) return {ok:false, note:'Write it as numbers multiplied together, like 2^2*3*7 or 2*2*3*7.'};
    if(sameMap(want,got) && allPrimeBases(got)) return {ok:true, note:''};
    if(mapValue(got)===mapValue(want) && !allPrimeBases(got)){
      if(Object.keys(got).length===1 && Object.values(got)[0]===1)
        return {ok:false, note:'That is the number itself. Break it into a product of primes.'};
      return {ok:false, note:'The product is right, but some pieces are still composite. Split them until every piece is prime.'};
    }
    if(mapValue(got)===mapValue(want)) return {ok:true, note:''};
    return {ok:false, note:'Multiply your pieces back up: you get '+mapValue(got)+', not '+mapValue(want)+'.'};
  }
  if(step.type==='num'){
    const ns=numsIn(raw);
    if(!ns.length) return {ok:false, note:'I need a number here.'};
    if(ns.some(n=>Math.abs(n-step.answer)<1e-9)) return {ok:true, note:''};
    const g=ns[0]; let note='';
    if(Math.abs(g-step.answer)<=2 || (step.answer!==0 && Math.abs(g-step.answer)/Math.abs(step.answer)<0.005))
      note='Very close \u2014 check one small piece of your arithmetic.';
    else note = g>step.answer ? 'That is bigger than the right value.' : 'That is smaller than the right value.';
    return {ok:false, note};
  }
  if(step.type==='nums'){
    const want=[...step.answer].sort((a,b)=>a-b);
    const got=[...new Set(numsIn(raw))].sort((a,b)=>a-b);
    if(got.length===want.length && got.every((n,i)=>Math.abs(n-want[i])<1e-9)) return {ok:true, note:''};
    if(want.every(w=>got.includes(w)) && got.length>want.length) return {ok:false, note:'You have the right ones plus something extra. Drop the extra.'};
    if(got.every(g=>want.includes(g)) && got.length<want.length) return {ok:false, note:'Right so far, but one is missing.'};
    if(got.length===want.length) return {ok:false, note:'Right number of values, but at least one of them is off.'};
    return {ok:false, note:'I am looking for '+want.length+' number'+(want.length>1?'s':'')+' here, and you gave '+got.length+'.'};
  }
  if(step.type==='choice'){
    const m=v.match(/[a-e]/);
    if(!m) return {ok:false, note:'Answer with a letter: A, B, C, D or E.'};
    return {ok:m[0]===String(step.answer).toLowerCase(), note:''};
  }
  if(step.type==='text'){
    if(step.reject && step.reject.some(r=>new RegExp(r,'i').test(v)))
      return {ok:false, note:step.rejectNote||''};
    const ok = step.re.some(r=>new RegExp(r,'i').test(v));
    if(!ok && step.near){ for(const [r,msg] of step.near) if(new RegExp(r,'i').test(v)) return {ok:false, note:msg}; }
    return {ok, note:''};
  }
  return {ok:false, note:''};
}
"""

JS_APP = r"""
/* ============ workbench ============ */
let APP=null, BY={}, ST={}, CUR=null, TAB='problem', STEP=0, T0=0, TIMER=null;
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const PRAISE=['Correct.','That is it.','Right.','Yes \u2014 that works.','Exactly right.'];

/* Deep links work when the page is served as a file or over http. Inside a
   sandboxed about:srcdoc frame the History API throws, so both directions are
   guarded and the app simply opens at the first problem. */
function wantedId(){
  try{ return (window.location.hash||'').replace('#',''); }catch(e){ return ''; }
}
function setHash(pid){
  try{
    if(window.location.protocol==='about:') return;
    if(window.history && window.history.replaceState)
      window.history.replaceState(null,'','#'+pid);
  }catch(e){ /* sandboxed frame: navigation state is not ours to change */ }
}

function boot(app){
  APP=app;
  if(app.startTab) TAB=app.startTab;
  app.problems.forEach(p=>{ BY[p.id]=p; ST[p.id]={steps:p.steps.map(()=>({attempts:0,state:'open',work:'',ans:''})),
    log:[], submitted:false, seconds:0, ink:[]}; });
  buildSide(); buildPicker();
  wire();
  open(BY[wantedId()] ? wantedId() : app.problems[0].id);
  TIMER=setInterval(()=>{ if(CUR){ ST[CUR].seconds++; paintStats(); } },1000);
}

function order(){ return APP.problems.map(p=>p.id); }
function stateOf(pid){
  const s=ST[pid].steps;
  if(s.every(x=>x.state==='solved')) return 'done';
  if(s.every(x=>x.state!=='open')) return 'closed';
  if(s.some(x=>x.state!=='open'||x.attempts>0)) return 'part';
  return 'open';
}
function mark(pid){
  const k=stateOf(pid);
  return k==='done' ? '\u2713' : k==='closed' ? '\u2713' : k==='part' ? '\u00b7\u00b7' : '\u25cb';
}

function buildSide(){
  let h='';
  APP.groups.forEach(g=>{
    h += '<h3>'+esc(g.title)+'</h3><ol>';
    g.items.forEach(pid=>{
      const p=BY[pid];
      h += '<li><button data-p="'+pid+'"><span class="dot" data-dot="'+pid+'">'+mark(pid)+'</span><span>'+esc(p.short||p.label)+'</span></button></li>';
    });
    h += '</ol>';
  });
  $('side').innerHTML=h;
  $('side').querySelectorAll('button[data-p]').forEach(b=>
    b.addEventListener('click',()=>{ open(b.dataset.p); $('side').classList.remove('open'); }));
}
function buildPicker(){
  let h='';
  APP.groups.forEach(g=>{
    h += '<optgroup label="'+esc(g.title)+'">';
    g.items.forEach(pid=>{ h += '<option value="'+pid+'">'+esc(BY[pid].label)+'</option>'; });
    h += '</optgroup>';
  });
  $('picker').innerHTML=h;
  $('picker').addEventListener('change',e=>open(e.target.value));
}

function wire(){
  $('prev').addEventListener('click',()=>hop(-1));
  $('next').addEventListener('click',()=>hop(1));
  $('navtoggle').addEventListener('click',()=>$('side').classList.toggle('open'));
  $('check').addEventListener('click',()=>check(STEP));
  $('hint').addEventListener('click',openHint);
  $('hintclose').addEventListener('click',closeHint);
  $('hintok').addEventListener('click',closeHint);
  $('mask').addEventListener('click',e=>{ if(e.target===$('mask')) closeHint(); });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape') closeHint(); });
  $('submit').addEventListener('click',submitAll);
  $('reveal').addEventListener('click',reveal);
  $('clearlog').addEventListener('click',()=>{ ST[CUR].log=[]; paintLog(); });
  $('work').addEventListener('input',()=>{ ST[CUR].steps[STEP].work=$('work').value; gutter(); });
  $('work').addEventListener('scroll',()=>{ $('gutter').scrollTop=$('work').scrollTop; });
  $('work').addEventListener('keydown',e=>{ if(e.key==='Enter'&&(e.ctrlKey||e.metaKey)){ e.preventDefault(); check(STEP); } });
  $('ans').addEventListener('input',()=>{ ST[CUR].steps[STEP].ans=$('ans').value; });
  $('ans').addEventListener('keydown',e=>{ if(e.key==='Enter'){ e.preventDefault(); check(STEP); } });
  document.querySelectorAll('.tabs button').forEach(b=>
    b.addEventListener('click',()=>{ TAB=b.dataset.tab; paintTabs(); paintDesc(); }));
}
function hop(d){
  const o=order(), i=o.indexOf(CUR)+d;
  if(i>=0 && i<o.length) open(o[i]);
}

function open(pid){
  if(CUR){ save(); if(window.INK) ST[CUR].ink=window.INK.get(); }
  CUR=pid; STEP=0;
  if(window.INK) window.INK.set(ST[pid].ink||[]);
  if(TAB==='concept' && !BY[pid].concept) TAB='problem';
  $('picker').value=pid;
  disarm();
  paintTabs(); paintDesc(); paintSteps(); paintLog(); paintStats(); paintSide();
  const o=order(); $('prev').disabled=o.indexOf(pid)===0; $('next').disabled=o.indexOf(pid)===o.length-1;
  setHash(pid);
  $('desc').scrollTop=0;
}
function save(){
  const s=ST[CUR].steps[STEP];
  if(s){ s.work=$('work').value; s.ans=$('ans').value; }
}

/* ---------- painting ---------- */
function paintTabs(){
  const hasC=!!BY[CUR].concept, hasR=!!APP.reference;
  document.querySelectorAll('.tabs button').forEach(b=>{
    const t=b.dataset.tab;
    b.style.display = (t==='concept'&&!hasC)||(t==='reference'&&!hasR) ? 'none':'';
    b.classList.toggle('on', t===TAB);
  });
}
function paintDesc(){
  const p=BY[CUR], s=ST[CUR];
  if(TAB==='concept'){ $('desc').innerHTML=p.concept; return; }
  if(TAB==='reference'){ $('desc').innerHTML=APP.reference; return; }
  if(TAB==='steps'){
    let h='<h1>'+esc(p.label)+'</h1><p class="dimtext">Your progress on each step.</p><ul class="steplist">';
    p.steps.forEach((st,i)=>{
      const x=s.steps[i];
      const ic = x.state==='solved' ? '<span class="ic ok">\u2713</span>' :
                 x.state==='given'  ? '<span class="ic giv">\u2192</span>' : '<span class="ic">\u25cb</span>';
      const word = x.state==='solved' ? (x.attempts===0?'right first try':'right after '+(x.attempts+1)+' tries')
                 : x.state==='given' ? 'answer was given \u2014 redo this one later'
                 : x.attempts? x.attempts+' tr'+(x.attempts===1?'y':'ies')+' used' : 'not started';
      h += '<li>'+ic+'<span><b>Step '+(i+1)+'.</b> '+st.ask+'<br><span class="chip">'+word+'</span></span></li>';
    });
    $('desc').innerHTML=h+'</ul>';
    return;
  }
  let h='<h1>'+esc(p.label)+'</h1><div class="chips">';
  (p.tags||[]).forEach(t=>{ h += '<span class="chip '+(t.k||'')+'">'+esc(t.t)+'</span>'; });
  h += '<span class="chip">'+p.steps.length+' steps</span></div>';
  h += '<div class="qbody">'+p.prompt+'</div>';
  if(p.src) h += '<p class="chip">'+esc(p.src)+'</p>';
  h += '<h2>How to work</h2><ol><li>Read the step showing on the right.</li>'+
       '<li>Write your working in the work area, then put the result in the answer box.</li>'+
       '<li><b>Check step</b> grades it. You get three tries, each with a nudge on what went wrong.</li>'+
       '<li>Stuck? <b>Hint for this step</b> opens a hint just for the step you are on \u2014 nothing appears unless you ask for it.</li>'+
       '<li>After three misses you get one final attempt.</li>'+
       '<li>Miss that one and the step answer is handed over \u2014 copy it and take the next step yourself.</li>'+
       '<li><b>Submit question</b> prints feedback on every step plus the verified answer.</li></ol>';
  $('desc').innerHTML=h;
}
function paintSide(){
  $('side').querySelectorAll('button[data-p]').forEach(b=>b.classList.toggle('on', b.dataset.p===CUR));
  APP.problems.forEach(p=>{
    const d=$('side').querySelector('[data-dot="'+p.id+'"]');
    if(!d) return;
    const k=stateOf(p.id);
    d.textContent=mark(p.id);
    d.className='dot'+(k==='done'||k==='closed'?' done':k==='part'?' part':'');
  });
}
function paintSteps(){
  const p=BY[CUR], s=ST[CUR];
  let h='';
  p.steps.forEach((st,i)=>{
    const x=s.steps[i];
    const cls = x.state==='solved'?'done':x.state==='given'?'giv':'';
    h += '<button data-s="'+i+'" class="'+cls+(i===STEP?' on':'')+'">step '+(i+1)+
         (x.state==='solved'?' \u2713':x.state==='given'?' \u2192':'')+'</button>';
  });
  $('steptabs').innerHTML=h;
  $('steptabs').querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
    save(); STEP=+b.dataset.s; disarm(); paintSteps(); }));

  const st=p.steps[STEP], x=s.steps[STEP];
  $('prompt').innerHTML='<span class="lab">step '+(STEP+1)+' of '+p.steps.length+'</span>'+st.ask;
  $('work').value=x.work;
  $('work').placeholder=(st.workHint||'write your reasoning here \u2026').replace(/\n/g,'\n');
  $('ans').value=x.ans;
  $('ans').placeholder=st.placeholder||'your answer';
  const locked = x.state!=='open';
  $('work').readOnly=locked; $('ans').readOnly=locked; $('check').disabled=locked;
  const left=Math.max(0,3-x.attempts);
  $('tries').innerHTML = (x.state==='solved' ? 'solved' : x.state==='given' ? 'answer shown' :
    x.attempts>=3 ? '<i>last try</i>' : left+' tr'+(left===1?'y':'ies')+' left')
    + (x.hinted ? '  \u00b7 hint used' : '');
  $('hint').disabled = x.state!=='open';
  gutter();
}
function gutter(){
  const n=Math.max(4, $('work').value.split('\n').length+1);
  let s=''; for(let i=1;i<=n;i++) s+=i+'\n';
  $('gutter').textContent=s;
  $('gutter').scrollTop=$('work').scrollTop;
}
function paintStats(){
  const done=APP.problems.filter(p=>stateOf(p.id)!=='open'&&ST[p.id].steps.every(x=>x.state!=='open')).length;
  $('done').innerHTML='<b>'+done+'</b> / '+APP.problems.length+' finished';
  const t=ST[CUR]?ST[CUR].seconds:0;
  $('clock').textContent=String(Math.floor(t/60)).padStart(2,'0')+':'+String(t%60).padStart(2,'0');
}
function paintLog(){
  const L=ST[CUR].log;
  $('log').innerHTML = L.length ? L.map(e=>'<p class="e '+e.c+'">'+e.t+'</p>').join('')
    : '<p class="e empty">Feedback appears here.\nWrite your working, put the result in the answer box, then press <b>Check step</b>.</p>';
  $('log').scrollTop=$('log').scrollHeight;
}
function say(c,t){ ST[CUR].log.push({c:c,t:t}); paintLog(); }

/* ---------- grading ---------- */
function check(i){
  save();
  const p=BY[CUR], s=ST[CUR], st=p.steps[i], x=s.steps[i];
  if(x.state!=='open') return;
  if(!x.ans.trim()){ say('bad','! step '+(i+1)+' \u2014 the answer box is empty. Put your result there, then check.'); return; }
  say('cmd','&gt;&gt;&gt; check step '+(i+1)+'  \u00b7  answer: '+esc(x.ans.trim()));
  if(!x.work.trim()) say('dim','(no working written \u2014 write the steps too, that is what gets you the marks)');

  const r=checkAnswer(st,x.ans);
  if(r.ok){
    x.state='solved';
    say('good','\u2713 '+PRAISE[i%PRAISE.length]+(st.why?' '+st.why:''));
    const nxt=p.steps[i+1];
    if(nxt){ say('dim','\u2192 move to step '+(i+2)+'.'); STEP=i+1; }
    else say('dim','\u2192 last step. Press Submit question for your feedback and the verified answer.');
    paintSteps(); paintSide(); paintStats();
    if(TAB==='steps') paintDesc();
    return;
  }
  x.attempts++;
  if(x.attempts<=3){
    const n=st.nudges[Math.min(x.attempts,st.nudges.length)-1];
    say('bad','\u2717 not yet.'+(r.note?' '+esc(r.note):'')+'\n   '+n);
    if(x.attempts===3) say('dim','   three tries used. One more attempt on this step \u2014 press <b>Hint for this step</b> first if you want it.');
    else say('dim','   fix your working above and check again.');
    paintSteps();
    return;
  }
  handOver(i,true);
}
function openHint(){
  const p=BY[CUR], st=p.steps[STEP], x=ST[CUR].steps[STEP];
  $('hintstep').textContent='step '+(STEP+1)+' of '+p.steps.length;
  $('hintq').innerHTML=st.ask;
  $('hinttext').innerHTML=st.hint;
  $('mask').classList.add('open');
  $('hintok').focus();
  if(!x.hinted){ x.hinted=true; say('hint','\u25c7 hint opened for step '+(STEP+1)+'. Tries are unaffected \u2014 go back and try again.'); }
}
function closeHint(){ $('mask').classList.remove('open'); }

function handOver(i,afterTry){
  const p=BY[CUR], s=ST[CUR], st=p.steps[i], x=s.steps[i];
  x.state='given';
  say('give',(afterTry?'\u2192 let me take this step with you. ':'\u2192 step '+(i+1)+' answer. ')+st.solution);
  const nxt=p.steps[i+1];
  if(nxt){ say('dim','   copy that into your working, then take step '+(i+2)+' yourself \u2014 '+(st.forward||'you have what you need now.')); STEP=i+1; }
  else say('dim','   that closes the problem. Read the verified answer, then redo this one from scratch tomorrow.');
  paintSteps(); paintSide(); paintStats();
  if(TAB==='steps') paintDesc();
}

function submitAll(){
  save();
  const p=BY[CUR], s=ST[CUR];
  p.steps.forEach((st,i)=>{ if(s.steps[i].state==='open' && s.steps[i].ans.trim()) check(i); });
  const open=s.steps.filter(x=>x.state==='open').length;
  say('head','&gt;&gt;&gt; submit '+esc(p.label));
  p.steps.forEach((st,i)=>{
    const x=s.steps[i];
    if(x.state==='solved') say('good','  \u2713 step '+(i+1)+': right '+(x.attempts===0?'first try':'after '+(x.attempts+1)+' tries'));
    else if(x.state==='given') say('give','  \u2192 step '+(i+1)+': answer was given to you. '+st.recheck);
    else say('dim','  \u25cb step '+(i+1)+': not checked yet');
  });
  if(open) say('dim','  '+open+' step'+(open>1?'s':'')+' still open \u2014 the verified answer stays locked until every step is closed.');
  else finalAnswer();
  s.submitted=true;
  paintStats();
}
let ARMED=false;
function disarm(){ ARMED=false; $('reveal').textContent='Show worked answer'; $('reveal').classList.remove('hintbtn'); }
function reveal(){
  save();
  const s=ST[CUR];
  const untouched=s.steps.some(x=>x.state==='open'&&x.attempts===0);
  if(untouched && !ARMED){
    ARMED=true;
    $('reveal').textContent='Click again to give up';
    $('reveal').classList.add('hintbtn');
    say('dim','\u25c7 some steps have not been tried yet. Click <b>Give up</b> again to open the full answer, or press <b>Hint for this step</b> instead.');
    return;
  }
  disarm();
  s.steps.forEach((x,i)=>{ if(x.state==='open') handOver(i,false); });
  finalAnswer();
}
function finalAnswer(){
  const p=BY[CUR];
  say('head','verified answer \u2014 '+esc(p.label)+'<span class="ans">'+p.answer+'</span>'+p.explain);
}
"""

HEAD = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style>
</head><body>
"""

SHELL = """
<header class="top">
  <button class="iconbtn navtoggle" id="navtoggle" aria-label="Show problem list">\u2630</button>
  <div class="brand"><span class="mark">\u00b7\u00b7</span><span>{brand}<small>{subtitle}</small></span></div>
  <div class="nav">
    <button class="iconbtn" id="prev" aria-label="Previous problem">\u2039</button>
    <button class="iconbtn" id="next" aria-label="Next problem">\u203a</button>
  </div>
  <select class="picker" id="picker" aria-label="Choose a problem">{picker0}</select>
  <span class="spacer"></span>
  <span class="stat" id="done"></span>
  <span class="stat" id="clock">00:00</span>
  <a class="stat" href="{other}">{otherlabel}</a>
</header>

<div class="shell">
  <nav class="pane side" id="side" aria-label="Problem list">{side0}</nav>

  <section class="pane">
    <div class="tabs" role="tablist">
      <button data-tab="problem"{on_problem}>Problem</button>
      <button data-tab="concept"{on_concept}>Concept</button>
      <button data-tab="reference">Rules</button>
      <button data-tab="steps">My steps</button>
    </div>
    <div class="desc" id="desc">{desc0}</div>
  </section>

  <section class="right">
    <div class="worktop">
      <div class="steptabs" id="steptabs">{steptabs0}</div>
      <div class="prompt" id="prompt">{prompt0}</div>
    </div>
    <div class="editwrap">
      <div class="gutter" id="gutter" aria-hidden="true">1\n2\n3\n4\n5</div>
      <textarea id="work" spellcheck="false" aria-label="Your working" placeholder="write your reasoning here \u2026"></textarea>
    </div>
    <div class="answerbar">
      <label for="ans">answer</label>
      <input id="ans" type="text" spellcheck="false" autocomplete="off">
      <button class="btn" id="check">Check step <small>\u21b5</small></button>
    </div>
    <div class="actionbar">
      <button class="btn hintbtn" id="hint">Hint for this step</button>
      <button class="btn ghost" id="submit">Submit question</button>
      <button class="btn ghost" id="reveal">Show worked answer</button>
      <span class="tries" id="tries"></span>
    </div>
    <div class="term">
      <div class="bar"><b>FEEDBACK</b> <span>step-by-step grader</span>
        <button id="clearlog">clear</button></div>
      <div class="log" id="log" aria-live="polite"><p class="e empty">Feedback appears here.\nWrite your working, put the result in the answer box, then press <b>Check step</b>.</p></div>
    </div>
  </section>
</div>

<div class="mask" id="mask" role="dialog" aria-modal="true" aria-labelledby="hinttitle">
  <div class="modal">
    <header><b id="hinttitle">Hint</b><span id="hintstep"></span>
      <button id="hintclose" aria-label="Close hint">\u00d7</button></header>
    <div class="body"><p class="q" id="hintq"></p><p id="hinttext"></p></div>
    <footer><button class="btn" id="hintok">Back to the problem</button>
      <span class="note">Asking for a hint does not use up a try.</span></footer>
  </div>
</div>
{ink_html}
"""

TAIL = """<script>{check}</script>
<script>{app}</script>
<script>{ink_js}</script>
<script>boot({data});</script>
</body></html>
"""




# ============================================================================
# Ink layer v2 — a teaching pen.
#   * two anchoring modes: "fixed" (freezes the page, for the app panes) and
#     "document" (scrolls with the content, for long reading pages)
#   * smoothed, speed-tapered strokes; highlighter; straight line; box
#   * palm rejection, undo/redo, PNG export, per-problem ink via window.INK
# ============================================================================

INK_CSS = r"""
.inkpad{position:fixed;inset:0;z-index:60;pointer-events:none;touch-action:none}
.inklive{position:fixed;inset:0;z-index:61;pointer-events:none;touch-action:none}
.inkpad.on{pointer-events:auto;cursor:crosshair}
.inkpad.doc.on{touch-action:pan-y}
.inktools{position:fixed;right:14px;bottom:14px;z-index:70;display:flex;flex-direction:column;
  align-items:flex-end;gap:8px;font-family:var(--mono,"IBM Plex Mono",monospace)}
.inktools .panel{display:none;background:#fff;border:1px solid #cfd9dc;border-radius:12px;
  box-shadow:0 10px 30px rgba(8,26,30,.20);padding:10px;gap:8px;flex-direction:column}
.inktools.open .panel{display:flex}
.inktools .line{display:flex;gap:7px;align-items:center;justify-content:flex-end}
.inktools button{font-family:inherit;font-size:12.5px;border:1px solid #cfd9dc;background:#fff;
  color:#11242b;border-radius:8px;padding:7px 10px;cursor:pointer;line-height:1.2;min-height:34px}
.inktools button:hover{background:#f1f6f6}
.inktools button.sel{border-color:#0d6b6e;background:#e3eeee;color:#094f52;font-weight:500}
.inktools .sw{width:30px;height:30px;border-radius:50%;padding:0;border:2px solid #fff;
  box-shadow:0 0 0 1px #cfd9dc;min-height:0}
.inktools .sw.sel{box-shadow:0 0 0 2px #0d6b6e}
.inktools .nib{width:38px;padding:0;display:grid;place-items:center}
.inktools .nib span{display:block;background:#11242b;border-radius:99px}
.inktools .pen{font-size:14px;padding:11px 16px;border-radius:99px;background:#11242b;color:#fff;
  border-color:#11242b;box-shadow:0 8px 22px rgba(8,26,30,.26)}
.inktools .pen.on{background:#b1820f;border-color:#b1820f}
.inktools .hint{font-size:11.5px;color:#4a626c;max-width:210px;text-align:right;line-height:1.4;margin:0}
@media print{.inktools{display:none}}
"""

INK_HTML = """
<canvas class="inkpad" id="inkpad" aria-hidden="true"></canvas>
<canvas class="inklive" id="inklive" aria-hidden="true"></canvas>
<div class="inktools" id="inktools">
  <div class="panel" id="inkpanel">
    <div class="line" role="group" aria-label="Ink colour">
      <button class="sw sel" style="background:#d1402c" data-ink-color="#d1402c" aria-label="Red"></button>
      <button class="sw" style="background:#0d6b6e" data-ink-color="#0d6b6e" aria-label="Teal"></button>
      <button class="sw" style="background:#b1820f" data-ink-color="#b1820f" aria-label="Amber"></button>
      <button class="sw" style="background:#11242b" data-ink-color="#11242b" aria-label="Black"></button>
    </div>
    <div class="line" role="group" aria-label="Thickness">
      <button class="nib sel" data-ink-width="2.6" aria-label="Thin"><span style="width:18px;height:2px"></span></button>
      <button class="nib" data-ink-width="5" aria-label="Medium"><span style="width:18px;height:4px"></span></button>
      <button class="nib" data-ink-width="9" aria-label="Thick"><span style="width:18px;height:8px"></span></button>
    </div>
    <div class="line" role="group" aria-label="Tool">
      <button class="sel" data-ink-tool="pen">pen</button>
      <button data-ink-tool="hi">marker</button>
      <button data-ink-tool="line">line</button>
      <button data-ink-tool="box">box</button>
      <button data-ink-tool="erase">erase</button>
    </div>
    <div class="line">
      <button id="inkundo" aria-label="Undo last stroke">undo</button>
      <button id="inkredo" aria-label="Redo">redo</button>
      <button id="inkclear" aria-label="Clear all ink">clear</button>
      <button id="inksave" aria-label="Save ink as a PNG">save</button>
    </div>
    <div class="line">
      <button id="inkpalm" aria-pressed="false" aria-label="Stylus only, ignore finger touches">stylus only</button>
    </div>
    <p class="hint" id="inkhint"></p>
  </div>
  <button class="pen" id="inkpen" aria-pressed="false">\u270e&nbsp; Pen</button>
</div>
"""

INK_JS = r"""
/* Teaching pen.

   Performance model: two viewport-sized canvases. Finished strokes live on the
   committed layer and are never redrawn while drawing; the stroke in progress
   is appended segment by segment to a live layer, so the per-frame cost is the
   handful of new points, not the whole page of ink. In document mode the ink is
   stored in page coordinates and the layers are re-rendered with a translate
   when the page scrolls, which keeps both canvases small and sharp instead of
   allocating one the height of the document.

   window.INK exposes get/set so the host page can hold ink per problem.
   data-ink-mode="document" on <body> anchors ink to the content. */
(function(){
  var cvC=document.getElementById('inkpad'), cvL=document.getElementById('inklive'),
      tools=document.getElementById('inktools'), penBtn=document.getElementById('inkpen'),
      hint=document.getElementById('inkhint'), palmBtn=document.getElementById('inkpalm');
  if(!cvC||!cvL) return;
  var cx=cvC.getContext('2d'), lx=cvL.getContext('2d');
  if(!cx||!lx) return;

  var DOC = (document.body.getAttribute('data-ink-mode')==='document');
  var strokes=[], undone=[], cur=null, drawn=0, on=false;
  var color='#d1402c', width=2.6, tool='pen', palm=false;
  var dpr=1, W=0, H=0, ox=0, oy=0, pending=false, needFull=false;

  hint.textContent = DOC
    ? 'Ink sticks to the page, so you can scroll while drawing. A finger scrolls; the pen draws.'
    : 'Drawing freezes the panes. Turn the pen off to scroll or type.';

  function scrollOff(){
    if(!DOC) return [0,0];
    return [window.pageXOffset||0, window.pageYOffset||0];
  }
  function frame(ctx){
    ctx.setTransform(dpr,0,0,dpr,-ox*dpr,-oy*dpr);
  }
  function geom(){
    dpr=Math.min(window.devicePixelRatio||1, 2);
    W=window.innerWidth; H=window.innerHeight;
    [cvC,cvL].forEach(function(c){
      c.width=Math.floor(W*dpr); c.height=Math.floor(H*dpr);
      c.style.width=W+'px'; c.style.height=H+'px';
    });
    var s=scrollOff(); ox=s[0]; oy=s[1];
    frame(cx); frame(lx);
    repaint();
  }
  function wipe(ctx,c){
    ctx.setTransform(1,0,0,1,0,0);
    ctx.clearRect(0,0,c.width,c.height);
    frame(ctx);
  }

  /* ---------- geometry of one stroke ---------- */
  function widthAt(a,b,base){
    var d=Math.abs(b.x-a.x)+Math.abs(b.y-a.y);
    var f=1-Math.min(d,34)/34*0.38;          /* faster stroke, finer line */
    return base*(0.66+0.34*f*1.2);
  }
  function penSeg(ctx,a,b,s){
    var w=widthAt(a,b,s.width);
    b.w = w = a.w ? (a.w*0.6+w*0.4) : w;
    ctx.strokeStyle=s.color; ctx.lineWidth=w; ctx.lineJoin=ctx.lineCap='round';
    ctx.beginPath();
    ctx.moveTo(a.x,a.y);
    ctx.quadraticCurveTo(a.x,a.y,(a.x+b.x)/2,(a.y+b.y)/2);
    ctx.lineTo(b.x,b.y);
    ctx.stroke();
  }
  function bandSeg(ctx,a,b,s,w,style,comp){
    ctx.globalCompositeOperation=comp||'source-over';
    ctx.globalAlpha = (s.tool==='hi') ? 0.30 : 1;
    ctx.strokeStyle=style; ctx.lineWidth=w; ctx.lineJoin=ctx.lineCap='round';
    ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
    ctx.globalAlpha=1; ctx.globalCompositeOperation='source-over';
  }
  function shape(ctx,s){
    var a=s.p[0], b=s.p[s.p.length-1];
    ctx.strokeStyle=s.color; ctx.lineWidth=s.width; ctx.lineJoin=ctx.lineCap='round';
    ctx.beginPath();
    if(s.tool==='line'){ ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); }
    else { ctx.rect(Math.min(a.x,b.x),Math.min(a.y,b.y),Math.abs(b.x-a.x),Math.abs(b.y-a.y)); }
    ctx.stroke();
  }
  /* draw stroke segments [from, end) onto ctx */
  function drawFrom(ctx,s,from){
    var p=s.p;
    if(!p.length) return;
    if(s.tool==='line'||s.tool==='box'){ shape(ctx,s); return; }
    if(p.length===1){
      var dot={x:p[0].x+0.01,y:p[0].y};
      if(s.tool==='erase') bandSeg(ctx,p[0],dot,s,Math.max(18,s.width*6),'rgba(0,0,0,1)','destination-out');
      else if(s.tool==='hi') bandSeg(ctx,p[0],dot,s,Math.max(14,s.width*4.5),s.color);
      else penSeg(ctx,p[0],dot,s);
      return;
    }
    for(var i=Math.max(1,from); i<p.length; i++){
      if(s.tool==='erase') bandSeg(ctx,p[i-1],p[i],s,Math.max(18,s.width*6),'rgba(0,0,0,1)','destination-out');
      else if(s.tool==='hi') bandSeg(ctx,p[i-1],p[i],s,Math.max(14,s.width*4.5),s.color);
      else penSeg(ctx,p[i-1],p[i],s);
    }
  }
  function repaint(){                       /* committed layer, whole page of ink */
    wipe(cx,cvC);
    for(var i=0;i<strokes.length;i++){ resetWidths(strokes[i]); drawFrom(cx,strokes[i],1); }
  }
  function resetWidths(s){ for(var i=0;i<s.p.length;i++) s.p[i].w=0; }

  /* ---------- frame loop: only the live stroke ---------- */
  function tick(){
    pending=false;
    if(needFull){ needFull=false; var s=scrollOff(); ox=s[0]; oy=s[1]; frame(cx); frame(lx); repaint();
      wipe(lx,cvL); if(cur){ resetWidths(cur); drawFrom(lx,cur,1); drawn=cur.p.length; } return; }
    if(!cur) return;
    if(cur.tool==='line'||cur.tool==='box'){ wipe(lx,cvL); shape(lx,cur); return; }
    if(cur.p.length>drawn){ drawFrom(lx,cur,Math.max(1,drawn)); drawn=cur.p.length; }
  }
  function schedule(){
    if(pending) return;
    pending=true;
    if(window.requestAnimationFrame) requestAnimationFrame(tick); else tick();
  }

  /* ---------- pointer ---------- */
  function pt(e){ return {x:e.clientX+ox, y:e.clientY+oy, w:0}; }
  function usable(e){ return on && !(palm && e.pointerType==='touch'); }

  cvC.addEventListener('pointerdown',function(e){
    if(!usable(e)) return;
    e.preventDefault();
    try{ cvC.setPointerCapture(e.pointerId); }catch(err){}
    var t = (e.shiftKey && (tool==='pen'||tool==='hi')) ? 'line' : tool;
    cur={tool:t,color:color,width:width,p:[pt(e)]};
    drawn=0; undone=[];
    schedule();
  });
  cvC.addEventListener('pointermove',function(e){
    if(!cur || !usable(e)) return;
    e.preventDefault();
    var list = (e.getCoalescedEvents && e.getCoalescedEvents().length) ? e.getCoalescedEvents() : [e];
    for(var i=0;i<list.length;i++){
      var q=pt(list[i]), last=cur.p[cur.p.length-1];
      if(cur.tool==='line'||cur.tool==='box') cur.p[1]=q;
      else if(Math.abs(q.x-last.x)+Math.abs(q.y-last.y) >= 1.1) cur.p.push(q);
    }
    schedule();
  });
  function commit(){
    if(!cur) return;
    /* one pass onto the committed layer, then the live layer is cheap to wipe */
    resetWidths(cur);
    drawFrom(cx,cur,1);
    strokes.push(cur);
    cur=null; drawn=0;
    wipe(lx,cvL);
  }
  cvC.addEventListener('pointerup',commit);
  cvC.addEventListener('pointercancel',commit);
  cvC.addEventListener('lostpointercapture',commit);
  cvC.addEventListener('wheel',function(e){ if(on && !DOC) e.preventDefault(); },{passive:false});
  cvC.addEventListener('touchmove',function(e){ if(on && !DOC) e.preventDefault(); },{passive:false});

  if(DOC) window.addEventListener('scroll',function(){ needFull=true; schedule(); },{passive:true});

  /* ---------- controls ---------- */
  function setPen(v){
    on=v;
    cvC.classList.toggle('on',on);
    if(DOC) cvC.classList.add('doc');
    tools.classList.toggle('open',on);
    penBtn.classList.toggle('on',on);
    penBtn.setAttribute('aria-pressed',on?'true':'false');
    penBtn.innerHTML = on ? '\u270e&nbsp; Pen on' : '\u270e&nbsp; Pen';
    document.body.style.userSelect = on ? 'none' : '';
    if(on){ needFull=true; schedule(); }
  }
  function pick(sel,el){
    var list=document.querySelectorAll(sel);
    for(var i=0;i<list.length;i++) list[i].classList.remove('sel');
    el.classList.add('sel');
  }
  penBtn.addEventListener('click',function(){ setPen(!on); });
  document.getElementById('inkundo').addEventListener('click',function(){
    if(strokes.length){ undone.push(strokes.pop()); repaint(); } });
  document.getElementById('inkredo').addEventListener('click',function(){
    if(undone.length){ strokes.push(undone.pop()); repaint(); } });
  document.getElementById('inkclear').addEventListener('click',function(){
    undone=strokes.slice().reverse(); strokes=[]; repaint(); });
  document.getElementById('inksave').addEventListener('click',function(){
    try{
      var out=document.createElement('canvas');
      out.width=cvC.width; out.height=cvC.height;
      var c2=out.getContext('2d');
      c2.fillStyle='#fff'; c2.fillRect(0,0,out.width,out.height);
      c2.drawImage(cvC,0,0); c2.drawImage(cvL,0,0);
      var a=document.createElement('a');
      a.download='ink.png'; a.href=out.toDataURL('image/png'); a.click();
    }catch(err){}
  });
  palmBtn.addEventListener('click',function(){
    palm=!palm; palmBtn.classList.toggle('sel',palm);
    palmBtn.setAttribute('aria-pressed',palm?'true':'false');
  });
  var cs=document.querySelectorAll('[data-ink-color]');
  for(var i=0;i<cs.length;i++) (function(b){
    b.addEventListener('click',function(){ color=b.getAttribute('data-ink-color'); pick('[data-ink-color]',b); });
  })(cs[i]);
  var ws=document.querySelectorAll('[data-ink-width]');
  for(var j=0;j<ws.length;j++) (function(b){
    b.addEventListener('click',function(){ width=parseFloat(b.getAttribute('data-ink-width')); pick('[data-ink-width]',b); });
  })(ws[j]);
  var ts=document.querySelectorAll('[data-ink-tool]');
  for(var k=0;k<ts.length;k++) (function(b){
    b.addEventListener('click',function(){ tool=b.getAttribute('data-ink-tool'); pick('[data-ink-tool]',b); });
  })(ts[k]);

  document.addEventListener('keydown',function(e){
    var t=e.target, typing = t && (t.tagName==='TEXTAREA'||t.tagName==='INPUT'||t.tagName==='SELECT');
    if(e.key==='Escape' && on){ setPen(false); return; }
    if(typing) return;
    if(e.key==='p'||e.key==='P') setPen(!on);
    if(on && (e.key==='z'||e.key==='Z') && (e.ctrlKey||e.metaKey)){
      e.preventDefault();
      if(e.shiftKey){ if(undone.length){ strokes.push(undone.pop()); repaint(); } }
      else if(strokes.length){ undone.push(strokes.pop()); repaint(); }
    }
  });
  window.addEventListener('resize',geom);
  window.addEventListener('load',geom);

  window.INK = {
    get:function(){ return strokes; },
    set:function(list){ strokes=list||[]; undone=[]; cur=null; wipe(lx,cvL); repaint(); },
    resize:geom,
    isOn:function(){ return on; }
  };
  geom();
})();
"""
