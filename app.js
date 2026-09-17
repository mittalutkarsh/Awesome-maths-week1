const fs=require('fs');
const a=fs.readFileSync('assets2.py','utf8');
const jsCheck=a.split('JS_CHECK = r"""')[1].split('"""')[0];
const jsApp=a.split('JS_APP = r"""')[1].split('"""')[0];
class N{
  constructor(id){this.id=id;this.value='';this._html='';this.style={};this.dataset={};this.h={};
    this._cls=new Set();this.scrollTop=0;this.scrollHeight=0;
    this.classList={add:c=>this._cls.add(c),remove:c=>this._cls.delete(c),
      toggle:(c,f)=>{f?this._cls.add(c):this._cls.delete(c)},contains:c=>this._cls.has(c)};}
  set innerHTML(v){this._html=String(v)} get innerHTML(){return this._html}
  set textContent(v){this._html=String(v)} get textContent(){return this._html}
  addEventListener(k,f){(this.h[k]=this.h[k]||[]).push(f)}
  click(){(this.h.click||[]).forEach(f=>f({}))}
  querySelectorAll(){return []}
  querySelector(){return null}
  scrollIntoView(){}
  focus(){}
}
const reg={};
const ids=['side','picker','prev','next','navtoggle','check','submit','reveal','clearlog','work','ans','desc','steptabs','prompt','gutter','tries','log','done','clock','hint','hintclose','hintok','mask','hintstep','hintq','hinttext'];
ids.forEach(i=>reg[i]=new N(i));
const tabs=['problem','concept','reference','steps'].map(t=>{const n=new N('tab-'+t);n.dataset.tab=t;return n;});
global.document={getElementById:i=>reg[i]||null, querySelectorAll:sel=>sel==='.tabs button'?tabs:[], addEventListener:()=>{}};
global.window={ location:{ get hash(){ return '#q5'; }, protocol:'about:' },
  history:{ replaceState:()=>{ throw new Error('SecurityError: about:srcdoc'); } } };
global.location=global.window.location;
global.confirm=()=>{throw new Error('confirm is blocked in sandboxed frames')};
global.setInterval=()=>0;
eval(jsCheck); eval(jsApp + '\nglobal.X={get BY(){return BY},get ST(){return ST},get CUR(){return CUR},set CUR(v){CUR=v},get STEP(){return STEP},set STEP(v){STEP=v}};');

const data=JSON.parse(fs.readFileSync('/tmp/app.json','utf8'));
let errs=0;
function run(app,tag){
  boot(app);
  // walk every problem, answer every step correctly
  app.problems.forEach(p=>{
    open(p.id);
    p.steps.forEach((s,i)=>{
      X.STEP=i; paintSteps();
      let v;
      if(s.type==='factor') v=s.answer;
      else if(s.type==='num') v=String(s.answer);
      else if(s.type==='nums') v=s.answer.join(', ');
      else if(s.type==='choice') v=String(s.answer);
      else v={yes:'yes',no:'no',odd:'odd',lcm:'lcm','december 4':'December 4',divisible:'N+1 is divisible by all',
              'no such primes exist':'no such primes exist'}[s.answer];
      reg.work.value='some working'; reg.ans.value=v;
      X.ST[p.id].steps[i].work='some working'; X.ST[p.id].steps[i].ans=v;
      check(i);
      if(X.ST[p.id].steps[i].state!=='solved'){errs++;console.log('NOT SOLVED',tag,p.id,i,JSON.stringify(v));}
    });
    submitAll();
    const log=X.ST[p.id].log.map(e=>e.t).join('\n');
    if(!log.includes('verified answer')){errs++;console.log('NO FINAL',tag,p.id);}
  });
  console.log(tag,'all-correct pass done. finished counter:',reg.done.innerHTML);
}
run(data.lesson,'LESSON');
run(data.practice,'PRACTICE');

// wrong-path test: 4 misses -> handover, then reveal + navigation
boot(data.practice);
open('q9'); X.STEP=1; paintSteps();
for(let k=1;k<=4;k++){ reg.ans.value='7'; X.ST.q9.steps[1].ans='7'; if(k===3){openHint();} X.ST.q9.steps[1].work='w'; reg.work.value='w'; check(1); }
const l=X.ST.q9.log.map(e=>e.c+': '+e.t.replace(/\n/g,' | ')).join('\n');
console.log(l);
if(X.ST.q9.steps[1].state!=='given'){errs++;console.log('NO HANDOVER');}
reveal();
console.log('after reveal states:',X.ST.q9.steps.map(s=>s.state).join(','));
hop(1); console.log('hop ->',X.CUR);
hop(-1); console.log('hop back ->',X.CUR);
TAB='concept'; paintTabs(); paintDesc(); console.log('concept tab len on practice (no concept):',reg.desc.innerHTML.length>0);

// reveal path with no attempts at all (sandbox-safe two-click)
boot(data.practice); open('q13');
reveal();
console.log('after 1st click states:', X.ST.q13.steps.map(z=>z.state).join(','), '| btn:', reg.reveal.textContent);
reveal();
console.log('after 2nd click states:', X.ST.q13.steps.map(z=>z.state).join(','));
console.log('final log has verified answer:', X.ST.q13.log.some(e=>e.t.includes('verified answer')));
// reveal after all solved should be immediate
boot(data.practice); open('q17');
X.ST.q17.steps.forEach((z,i)=>{ z.state='solved'; });
reveal();
console.log('solved-case immediate:', X.ST.q17.log.some(e=>e.t.includes('verified answer')));
console.log('ERRS',errs);
