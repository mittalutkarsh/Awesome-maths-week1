CSS = r"""
:root{
  --ink:#10242b; --ink-soft:#3d5560; --paper:#eef2f3; --card:#ffffff;
  --rule:#d2dbdf; --teal:#0d6b6e; --teal-dark:#094f52; --gold:#b1820f; --gold-soft:#fff5dd;
  --ok:#146b47; --ok-soft:#e5f4ec; --no:#a32c1e; --no-soft:#fbeae7;
  --focus:#0d6b6e;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; color:var(--ink); background-color:var(--paper);
  background-image:
    linear-gradient(to right, rgba(13,107,110,.07) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(13,107,110,.07) 1px, transparent 1px);
  background-size:26px 26px;
  font-family:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;
  font-size:17.5px; line-height:1.62;
}
main{max-width:860px;margin:0 auto;padding:0 20px 90px}
h1,h2,h3{font-family:Fraunces,Georgia,"Times New Roman",serif;line-height:1.14;letter-spacing:-.01em}
h1{font-size:clamp(34px,6vw,54px);font-weight:700;margin:0 0 10px}
h2{font-size:clamp(25px,4vw,34px);font-weight:600;margin:0 0 6px}
h3{font-size:21px;font-weight:600;margin:26px 0 6px}
p{margin:0 0 14px;max-width:68ch}
a{color:var(--teal-dark);text-decoration-thickness:1px;text-underline-offset:3px}
.m{font-family:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;font-size:.94em;background:#f2f6f6;
   border:1px solid #dfe8e8;border-radius:4px;padding:1px 5px;white-space:nowrap}
sup{font-size:.68em}

/* ---------- masthead ---------- */
header.top{padding:34px 0 26px}
.kicker{font-size:15px;color:var(--teal-dark);margin:0 0 14px}
.kicker b{font-weight:700}
.lede{font-size:19px;color:var(--ink-soft);max-width:60ch}
.hero{background:var(--card);border:1px solid var(--rule);border-radius:3px;
      padding:18px 16px 10px;margin:22px 0 10px;box-shadow:0 1px 0 #dbe3e6}
.hero figcaption{font-size:14.5px;color:var(--ink-soft);padding:6px 4px 4px;max-width:none}
.hero svg{width:100%;height:auto;display:block}
@media (prefers-reduced-motion:no-preference){
  .grow{opacity:0;animation:grow .5s ease forwards}
  @keyframes grow{from{opacity:0;transform:translateY(-7px)}to{opacity:1;transform:none}}
}

/* ---------- section scaffolding ---------- */
section.lesson{background:var(--card);border:1px solid var(--rule);border-radius:3px;
  padding:26px 26px 30px;margin:26px 0;box-shadow:0 1px 0 #dbe3e6}
.tag{display:inline-block;font-size:14px;color:var(--teal-dark);border-bottom:2px solid var(--gold);
  padding-bottom:2px;margin-bottom:12px}
ul,ol{max-width:66ch;padding-left:22px}
li{margin:5px 0}
.rulebox{border-left:4px solid var(--gold);background:var(--gold-soft);padding:12px 16px;margin:16px 0;border-radius:0 3px 3px 0}
.rulebox p:last-child{margin:0}
.rulebox b{font-weight:700}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:620px){.two{grid-template-columns:1fr}}
.stack{background:#f7fafa;border:1px solid #e3ebeb;border-radius:3px;padding:12px 14px;
  font-family:"IBM Plex Mono",monospace;font-size:15px;line-height:1.8;overflow-x:auto;
  white-space:pre-wrap;tab-size:2}
table.cmp{border-collapse:collapse;width:100%;font-size:16px;margin:14px 0}
table.cmp th,table.cmp td{border:1px solid var(--rule);padding:8px 10px;text-align:left}
table.cmp th{background:#f1f6f6;font-weight:700}
nav.toc{background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:18px 22px;margin:22px 0}
nav.toc ol{columns:2;column-gap:28px;margin:0;font-size:16px;list-style-position:inside;padding-left:0}
@media(max-width:620px){nav.toc ol{columns:1}}
.jump{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 0}
.jump a{background:var(--teal);color:#fff;text-decoration:none;padding:10px 16px;border-radius:3px;font-size:16px}
.jump a.alt{background:#fff;color:var(--teal-dark);border:1px solid var(--teal)}

/* ---------- progress ---------- */
.bar{position:sticky;top:0;z-index:20;background:rgba(238,242,243,.94);backdrop-filter:blur(4px);
  border-bottom:1px solid var(--rule);padding:8px 20px;display:flex;align-items:center;gap:12px;font-size:15px}
.bar .track{flex:1;height:7px;background:#dde5e7;border-radius:99px;overflow:hidden;max-width:420px}
.bar .fill{height:100%;width:0;background:var(--teal);transition:width .3s ease}
.bar a{margin-left:auto;font-size:15px}

/* ---------- problem cards ---------- */
.prob{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--teal);
  border-radius:3px;padding:20px 22px 22px;margin:22px 0;box-shadow:0 1px 0 #dbe3e6}
.prob.done{border-left-color:var(--ok)}
.prob > h4{font-family:Fraunces,Georgia,serif;font-size:19px;margin:0 0 4px;font-weight:600}
.prob .qtext{font-size:18px;margin:0 0 6px}
.prob .qtext em{background:#fff5dd}
.src{font-size:14px;color:var(--ink-soft);margin:0 0 14px}

.step{border-top:1px dashed var(--rule);padding:16px 0 4px}
.step:first-of-type{border-top:1px solid var(--rule);margin-top:10px}
.step .ask{position:relative;padding-left:36px;margin-bottom:8px}
.step .n{position:absolute;left:0;top:2px;width:26px;height:26px;line-height:26px;text-align:center;
  border-radius:50%;background:var(--teal);color:#fff;font-size:14px;font-family:"IBM Plex Mono",monospace}
.step.solved .n{background:var(--ok)}
.step.given .n{background:var(--gold)}
.step .ask p{margin:0;font-size:17px}
label.work{display:block;font-size:14.5px;color:var(--ink-soft);margin:2px 0 4px 36px}
.step textarea{width:calc(100% - 36px);margin-left:36px;min-height:62px;resize:vertical;
  font-family:"IBM Plex Mono",monospace;font-size:15px;padding:9px 11px;border:1px solid var(--rule);
  border-radius:3px;background:#fcfdfd;color:var(--ink)}
.row{display:flex;gap:10px;align-items:center;margin:10px 0 0 36px;flex-wrap:wrap}
.row input{flex:1 1 200px;min-width:0;font-family:"IBM Plex Mono",monospace;font-size:16px;
  padding:10px 12px;border:1px solid var(--rule);border-radius:3px;background:#fcfdfd;color:var(--ink)}
button{font-family:inherit;font-size:16px;padding:10px 16px;border-radius:3px;border:1px solid var(--teal);
  background:var(--teal);color:#fff;cursor:pointer}
button.ghost{background:#fff;color:var(--teal-dark)}
button.link{background:none;border:none;color:var(--teal-dark);text-decoration:underline;padding:6px 0;font-size:15px}
button:disabled{opacity:.45;cursor:not-allowed}
button:hover:not(:disabled){background:var(--teal-dark);border-color:var(--teal-dark);color:#fff}
button.link:hover:not(:disabled){background:none;color:var(--ink)}
input:focus-visible,textarea:focus-visible,button:focus-visible,a:focus-visible{
  outline:3px solid var(--focus);outline-offset:2px}
.tries{font-size:14px;color:var(--ink-soft);font-family:"IBM Plex Mono",monospace}
.msg{margin:10px 0 0 36px;padding:10px 13px;border-radius:3px;font-size:16px;display:none}
.msg.show{display:block}
.msg.good{background:var(--ok-soft);border-left:4px solid var(--ok)}
.msg.bad{background:var(--no-soft);border-left:4px solid var(--no)}
.msg.hint{background:var(--gold-soft);border-left:4px solid var(--gold)}
.msg.give{background:#eef4f7;border-left:4px solid var(--teal)}
.msg b{font-weight:700}
.foot{border-top:1px solid var(--rule);margin-top:18px;padding-top:14px;display:flex;gap:10px;
  align-items:center;flex-wrap:wrap}
.report{display:none;margin-top:14px;border:1px solid var(--rule);border-radius:3px;overflow:hidden}
.report.show{display:block}
.report h5{margin:0;padding:10px 14px;background:#f1f6f6;font-size:16px;font-family:Fraunces,Georgia,serif;
  border-bottom:1px solid var(--rule)}
.report ul{list-style:none;margin:0;padding:10px 14px;font-size:16px;max-width:none}
.report li{margin:6px 0;padding-left:26px;position:relative}
.report li .ic{position:absolute;left:0;font-family:"IBM Plex Mono",monospace}
.final{padding:12px 14px;border-top:1px solid var(--rule);background:#fbfdfd;font-size:16.5px}
.final .ans{font-family:"IBM Plex Mono",monospace;font-size:16px;background:var(--gold-soft);
  border:1px solid #f0dfb4;border-radius:3px;padding:8px 10px;margin:8px 0;display:block;overflow-x:auto}
.final .why{color:var(--ink-soft);font-size:15.5px}
footer.end{text-align:center;color:var(--ink-soft);font-size:15px;padding:30px 0 0}
"""

JS = r"""
/* ============ tiny math helpers ============ */
const SUP = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4','\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9'};
function deSup(s){
  let out=''; let run='';
  for(const ch of String(s)){
    if(SUP[ch]){ run += SUP[ch]; }
    else { if(run){ out += '^'+run; run=''; } out += ch; }
  }
  if(run) out += '^'+run;
  return out;
}
function norm(s){ return deSup(s).toLowerCase().replace(/,/g,'').replace(/\s+/g,' ').trim(); }
function isPrime(n){
  if(n<2) return false;
  for(let d=2; d*d<=n; d++) if(n%d===0) return false;
  return true;
}
function numsIn(s){ return (norm(s).match(/\d+(?:\.\d+)?/g)||[]).map(Number); }

/* "2^3*5*11" | "2*2*2*5*11" | "2\u00b3\u00b75\u00b711" | "440 = 2^3 x 5 x 11"  ->  {2:3,5:1,11:1} */
function parseFactor(str){
  let s = deSup(str).toLowerCase();
  if(s.indexOf('=')>=0) s = s.split('=').pop();
  s = s.replace(/[\u00d7\u22c5\u00b7\u2219\u2715\u2022]/g,'*').replace(/\bx\b/g,'*')
       .replace(/\*\*/g,'^').replace(/\s+/g,'').replace(/[()]/g,'');
  if(!s) return null;
  const toks = s.split('*').filter(t=>t.length);
  if(!toks.length) return null;
  const map = {};
  for(const t of toks){
    const m = t.match(/^(\d+)(?:\^(\d+))?$/);
    if(!m) return null;
    const b = parseInt(m[1],10), e = m[2]?parseInt(m[2],10):1;
    if(b===1) continue;
    if(b<1) return null;
    map[b] = (map[b]||0)+e;
  }
  return map;
}
function mapValue(map){ let v=1; for(const b in map) v *= Math.pow(+b, map[b]); return v; }
function sameMap(a,b){
  const ka=Object.keys(a), kb=Object.keys(b);
  if(ka.length!==kb.length) return false;
  return ka.every(k=>a[k]===b[k]);
}
function allPrimeBases(map){ return Object.keys(map).every(b=>isPrime(+b)); }
function prettyFactor(str){
  return deSup(str).replace(/\*/g,' \u00b7 ').replace(/\^(\d+)/g,(m,d)=>
    d.split('').map(c=>'\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079'[+c]).join(''));
}

/* ============ answer checking ============ */
/* returns {ok:bool, note:string|''}  — note is an extra targeted remark */
function checkAnswer(step, raw){
  const v = norm(raw);
  if(!v) return {ok:false, note:'Type something in the answer box first.'};
  if(step.type==='factor'){
    const want = parseFactor(step.answer);
    const got  = parseFactor(raw);
    if(!got) return {ok:false, note:'Write it as numbers multiplied together, like 2^2*3*7 or 2*2*3*7.'};
    if(sameMap(want,got) && allPrimeBases(got)) return {ok:true, note:''};
    if(mapValue(got)===mapValue(want) && !allPrimeBases(got)){
      if(Object.keys(got).length===1 && Object.values(got)[0]===1)
        return {ok:false, note:'That is the number itself. Break it into a product of primes.'};
      return {ok:false, note:'The product is right, but some pieces are still composite. Split them until every piece is prime.'};
    }
    if(mapValue(got)===mapValue(want)) return {ok:true, note:''};
    return {ok:false, note:'Multiply your pieces back up: you get ' + mapValue(got) + ', not ' + mapValue(want) + '.'};
  }
  if(step.type==='num'){
    const ns = numsIn(raw);
    if(!ns.length) return {ok:false, note:'I need a number here.'};
    if(ns.some(n=>Math.abs(n-step.answer)<1e-9)) return {ok:true, note:''};
    const g = ns[0];
    let note='';
    if(Math.abs(g-step.answer)<1e-9) note='';
    else if(Math.abs(g-step.answer)<=2 || (step.answer!==0 && Math.abs(g-step.answer)/Math.abs(step.answer)<0.005)) note='Very close \u2014 check one small piece of your arithmetic.';
    else if(g>step.answer) note='That is bigger than the right value.';
    else note='That is smaller than the right value.';
    return {ok:false, note};
  }
  if(step.type==='nums'){
    const want=[...step.answer].sort((a,b)=>a-b);
    const got=[...new Set(numsIn(raw))].sort((a,b)=>a-b);
    if(got.length===want.length && got.every((n,i)=>Math.abs(n-want[i])<1e-9)) return {ok:true, note:''};
    if(want.every(w=>got.includes(w)) && got.length>want.length) return {ok:false, note:'You have the right ones plus something extra. Drop the extra.'};
    if(got.every(g=>want.includes(g)) && got.length<want.length) return {ok:false, note:'Right so far, but one is missing.'};
    if(got.length===want.length) return {ok:false, note:'Right number of values, but at least one of them is off.'};
    return {ok:false, note:'I am looking for ' + want.length + ' number' + (want.length>1?'s':'') + ' here, and you gave ' + got.length + '.'};
  }
  if(step.type==='choice'){
    const m = v.match(/[a-e]/);
    if(!m) return {ok:false, note:'Answer with a letter: A, B, C, D or E.'};
    return {ok: m[0]===String(step.answer).toLowerCase(), note:''};
  }
  if(step.type==='text'){
    if(step.reject && step.reject.some(r=>new RegExp(r,'i').test(v)))
      return {ok:false, note: step.rejectNote || ''};
    const ok = step.re.some(r=>new RegExp(r,'i').test(v));
    if(!ok && step.near) {
      for(const [r,msg] of step.near) if(new RegExp(r,'i').test(v)) return {ok:false, note:msg};
    }
    return {ok, note:''};
  }
  return {ok:false, note:''};
}

/* ============ rendering ============ */
const PRAISE = ['Correct.','That is it.','Right.','Yes \u2014 that works.','Exactly right.'];
let STATE = {total:0, done:0};

function el(tag, cls, html){
  const e=document.createElement(tag);
  if(cls) e.className=cls;
  if(html!==undefined) e.innerHTML=html;
  return e;
}

function buildProblem(p, idx){
  const card = el('section','prob');
  card.id = p.id;
  card.appendChild(el('h4',null, p.label || ('Problem '+(idx+1))));
  card.appendChild(el('p','qtext', p.prompt));
  if(p.src) card.appendChild(el('p','src', p.src));

  const stepEls = [];
  p.steps.forEach((st,i)=>{
    const s = el('div','step');
    const ask = el('div','ask');
    ask.appendChild(el('span','n', String(i+1)));
    ask.appendChild(el('p',null, st.ask));
    s.appendChild(ask);

    const wid = p.id+'-w'+i;
    const lab = el('label','work','Show your steps (write your thinking here)');
    lab.setAttribute('for', wid);
    s.appendChild(lab);
    const ta = el('textarea'); ta.id=wid; ta.placeholder = (st.workHint || 'write your reasoning here \u2026').replace(/\n/g,'   \u00b7   ');
    s.appendChild(ta);

    const row = el('div','row');
    const inp = el('input'); inp.type='text';
    inp.placeholder = st.placeholder || 'your answer';
    inp.setAttribute('aria-label','Answer for step '+(i+1));
    const btn = el('button',null,'Check this step');
    const tries = el('span','tries','3 tries left');
    row.appendChild(inp); row.appendChild(btn); row.appendChild(tries);
    s.appendChild(row);

    const msg = el('div','msg');
    s.appendChild(msg);

    const rec = {def:st, node:s, input:inp, btn:btn, tries:tries, msg:msg, attempts:0, state:'open'};
    stepEls.push(rec);

    btn.addEventListener('click', ()=> checkStep(p, stepEls, i));
    inp.addEventListener('keydown', e=>{ if(e.key==='Enter'){ e.preventDefault(); checkStep(p, stepEls, i); } });
    card.appendChild(s);
  });

  const foot = el('div','foot');
  const sub = el('button',null,'Submit all steps');
  const give = el('button','link','Show me the worked answer');
  foot.appendChild(sub); foot.appendChild(give);
  card.appendChild(foot);

  const report = el('div','report');
  card.appendChild(report);

  sub.addEventListener('click', ()=>{
    stepEls.forEach((r,i)=>{ if(r.state==='open' && r.input.value.trim()) checkStep(p, stepEls, i, true); });
    showReport(p, stepEls, report, card);
  });
  give.addEventListener('click', ()=>{
    const untouched = stepEls.some(r=>r.state==='open' && r.attempts===0);
    if(untouched && !confirm('You have steps you have not tried yet. Try them first \u2014 open the answer anyway?')) return;
    stepEls.forEach((r,i)=>{ if(r.state==='open') revealStep(p, stepEls, i); });
    showReport(p, stepEls, report, card, true);
  });

  return card;
}

function setTries(rec){
  const left = Math.max(0, 3-rec.attempts);
  if(rec.state==='solved'){ rec.tries.textContent='solved'; }
  else if(rec.state==='given'){ rec.tries.textContent='answer shown'; }
  else if(rec.attempts>=3){ rec.tries.textContent='last try'; }
  else rec.tries.textContent = left + ' tr' + (left===1?'y':'ies') + ' left';
}

function checkStep(p, recs, i, quiet){
  const rec = recs[i];
  if(rec.state!=='open') return;
  const st = rec.def;
  const res = checkAnswer(st, rec.input.value);

  if(!rec.input.value.trim()){
    rec.msg.className='msg bad show';
    rec.msg.innerHTML = 'Type your answer in the box, then check.';
    return;
  }

  if(res.ok){
    rec.state='solved';
    rec.node.classList.add('solved');
    rec.input.readOnly=true; rec.btn.disabled=true;
    rec.msg.className='msg good show';
    rec.msg.innerHTML = '<b>'+PRAISE[i%PRAISE.length]+'</b> ' + (st.why||'') +
      (recs[i+1] ? ' <span class="why">Now move to step '+(i+2)+'.</span>' : ' <span class="why">That was the last step \u2014 hit <b>Submit all steps</b>.</span>');
    setTries(rec); tickProgress(p, recs);
    return;
  }

  rec.attempts++;
  const n = rec.attempts;
  if(n<=3){
    const nudge = st.nudges[Math.min(n,st.nudges.length)-1];
    rec.msg.className='msg bad show';
    rec.msg.innerHTML = '<b>Not yet.</b> ' + (res.note? res.note+' ' : '') + nudge +
      (n===3 ? '' : ' <span class="why">Fix your steps above and check again.</span>');
    if(n===3){
      rec.msg.innerHTML += '<div style="margin-top:9px;padding-top:9px;border-top:1px solid #e6c9c3">' +
        '<b>Hint:</b> ' + st.hint + ' <span class="why">One more try \u2014 this one counts.</span></div>';
    }
    setTries(rec);
    return;
  }
  /* 4th attempt, after the hint, still wrong -> hand over this step */
  revealStep(p, recs, i, true);
}

function revealStep(p, recs, i, afterTry){
  const rec = recs[i]; const st = rec.def;
  rec.state='given';
  rec.node.classList.add('given');
  rec.input.readOnly=true; rec.btn.disabled=true;
  rec.msg.className='msg give show';
  rec.msg.innerHTML = (afterTry? '<b>Let me take this step with you.</b> ' : '<b>Step answer.</b> ') +
    st.solution +
    (recs[i+1] ? ' <span class="why">Copy that down, then take step '+(i+2)+' yourself \u2014 '+(st.forward||'you have what you need now.')+'</span>'
               : ' <span class="why">That closes the problem. Read the worked answer below, then try a similar one again tomorrow.</span>');
  setTries(rec); tickProgress(p, recs);
}

function tickProgress(p, recs){
  if(recs.every(r=>r.state!=='open')){
    if(!p._counted){ p._counted=true; STATE.done++; }
    const card = document.getElementById(p.id);
    if(card) card.classList.add('done');
  }
  const fill=document.getElementById('fill'), txt=document.getElementById('ptxt');
  if(fill) fill.style.width = (100*STATE.done/STATE.total)+'%';
  if(txt) txt.textContent = STATE.done + ' of ' + STATE.total + ' finished';
}

function showReport(p, recs, node, card, forced){
  const open = recs.filter(r=>r.state==='open').length;
  const ul = el('ul');
  recs.forEach((r,i)=>{
    let ic='\u25cb', word='not checked yet';
    if(r.state==='solved'){ ic='\u2713'; word = r.attempts===0 ? 'right first try' : 'right after '+(r.attempts+1)+' tries'; }
    else if(r.state==='given'){ ic='\u2192'; word='answer given to you \u2014 redo this one later'; }
    const li = el('li', null, '<span class="ic">'+ic+'</span><b>Step '+(i+1)+':</b> '+word+
      (r.state==='given' ? ' <span class="why">'+r.def.recheck+'</span>' : ''));
    ul.appendChild(li);
  });
  node.innerHTML='';
  node.appendChild(el('h5', null, open? 'Step feedback (you still have '+open+' step'+(open>1?'s':'')+' open)' : 'Step feedback'));
  node.appendChild(ul);
  if(!open || forced){
    const f = el('div','final');
    f.innerHTML = '<b>Verified answer.</b><span class="ans">'+p.answer+'</span>'+
                  '<div class="why">'+p.explain+'</div>';
    node.appendChild(f);
  }
  node.classList.add('show');
  node.scrollIntoView({block:'nearest', behavior:'smooth'});
}

function mountProblems(list, targetId){
  const host = document.getElementById(targetId);
  STATE.total += list.length;
  list.forEach((p,i)=>{ host.appendChild(buildProblem(p, i)); });
  const txt=document.getElementById('ptxt');
  if(txt) txt.textContent = STATE.done + ' of ' + STATE.total + ' finished';
}
"""

HEAD = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style>
</head><body>
"""

TAIL = """<script>{js}</script>
<script>{data}</script>
</body></html>
"""
