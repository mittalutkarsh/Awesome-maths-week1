const fs=require('fs');
const a=fs.readFileSync('assets2.py','utf8');
const ink=a.split('INK_JS = r"""')[1].split('"""')[0];
let stats={clearC:0,clearL:0,strokeC:0,strokeL:0};
function mkctx(tag){return {
  setTransform(){}, clearRect(){stats['clear'+tag]++}, beginPath(){}, moveTo(){}, lineTo(){},
  quadraticCurveTo(){}, rect(){}, stroke(){stats['stroke'+tag]++}, fillRect(){}, drawImage(){},
  set strokeStyle(v){}, set lineWidth(v){}, set lineJoin(v){}, set lineCap(v){},
  set globalAlpha(v){}, set globalCompositeOperation(v){}, set fillStyle(v){}};}
class N{constructor(tag,id){this.tag=tag;this.id=id;this.h={};this._cls=new Set();this.style={};this.attrs={};
  this.classList={add:c=>this._cls.add(c),remove:c=>this._cls.delete(c),
    toggle:(c,f)=>{(f===undefined?!this._cls.has(c):f)?this._cls.add(c):this._cls.delete(c)},contains:c=>this._cls.has(c)};}
  addEventListener(k,f){(this.h[k]=this.h[k]||[]).push(f)}
  fire(k,e){(this.h[k]||[]).forEach(f=>f(Object.assign({preventDefault(){}},e||{})))}
  setAttribute(k,v){this.attrs[k]=v} getAttribute(k){return this.attrs[k]||null}
  setPointerCapture(){} click(){} toDataURL(){return 'data:,'}
  getContext(){ return this.id==='inkpad'?mkctx('C'):this.id==='inklive'?mkctx('L'):mkctx('X'); }
  set innerHTML(v){this._h=v} get innerHTML(){return this._h}
  set textContent(v){this._t=v} get textContent(){return this._t}}
const reg={};
['inkpad','inklive','inktools','inkpen','inkundo','inkredo','inkclear','inksave','inkpalm','inkpanel','inkhint']
  .forEach(i=>reg[i]=new N(i.indexOf('ink')===0?'canvas':'div',i));
const colors=[new N('button')], widths=[new N('button')], tls=['pen','line','box','erase','hi'].map(t=>{const n=new N('button');n.setAttribute('data-ink-tool',t);return n;});
colors[0].setAttribute('data-ink-color','#d1402c'); widths[0].setAttribute('data-ink-width','2.6');
const body=new N('body'); let MODE='document'; body.getAttribute=k=>k==='data-ink-mode'?MODE:null;
let rafQ=[];
global.document={getElementById:i=>reg[i]||null,
  querySelectorAll:s=>s==='[data-ink-color]'?colors:s==='[data-ink-width]'?widths:s==='[data-ink-tool]'?tls:[],
  addEventListener:(k,f)=>{(global.docH=global.docH||{})[k]=f}, createElement:t=>new N(t),
  body, documentElement:{clientWidth:1200,scrollHeight:9000,offsetHeight:9000}};
global.window={devicePixelRatio:3,innerWidth:1200,innerHeight:800,pageXOffset:0,pageYOffset:2000,
  addEventListener:(k,f)=>{(global.winH=global.winH||{})[k]=f},
  requestAnimationFrame:f=>{rafQ.push(f);return rafQ.length}};
global.requestAnimationFrame=global.window.requestAnimationFrame;
function flush(){const q=rafQ;rafQ=[];q.forEach(f=>f());}
eval(ink);
const pad=reg.inkpad;
console.log('dpr capped at 2 ->', pad.width, 'x', pad.height, '(viewport-sized, not 9000 tall)');
console.log('canvas megapixels:', (pad.width*pad.height/1e6).toFixed(1));
reg.inkpen.fire('click'); flush();
stats={clearC:0,clearL:0,strokeC:0,strokeL:0};
// lay down 40 committed strokes of 50 points each
for(let s=0;s<40;s++){
  pad.fire('pointerdown',{clientX:10,clientY:10,pointerId:1,pointerType:'pen'});
  for(let i=0;i<50;i++){ pad.fire('pointermove',{clientX:10+i*3,clientY:10+i*2,pointerId:1,pointerType:'pen'}); flush(); }
  pad.fire('pointerup',{});
}
console.log('40 strokes x 50 pts -> committed strokes:', window.INK.get().length);
const before={...stats};
// now draw one more stroke and count work per frame
stats={clearC:0,clearL:0,strokeC:0,strokeL:0};
pad.fire('pointerdown',{clientX:5,clientY:5,pointerId:2,pointerType:'pen'});
for(let i=0;i<20;i++){ pad.fire('pointermove',{clientX:5+i*4,clientY:5+i,pointerId:2,pointerType:'pen'}); flush(); }
console.log('while drawing over 2000 existing points: committed clears =',stats.clearC,
            '| committed strokes redrawn =',stats.strokeC, '| live segments =',stats.strokeL);
pad.fire('pointerup',{});
// scroll triggers exactly one full repaint
stats={clearC:0,clearL:0,strokeC:0,strokeL:0};
global.window.pageYOffset=2600; global.winH.scroll ? global.winH.scroll() : null;
for(let i=0;i<5;i++){ global.winH.scroll && global.winH.scroll(); }
flush();
console.log('five scroll events -> full repaints:', stats.clearC);
MODE='fixed'; eval(ink);
console.log('fixed mode has no scroll listener redraw:', reg.inkpad.height===1600);

// ---- behaviour re-checks on the new renderer (document mode) ----
MODE='document'; global.window.pageYOffset=1500; eval(ink);
const P=reg.inkpad;
reg.inkpen.fire('click'); flush();
P.fire('pointerdown',{clientX:100,clientY:100,pointerId:1,pointerType:'pen'});
P.fire('pointermove',{clientX:140,clientY:130,pointerId:1,pointerType:'pen'}); flush();
P.fire('pointerup',{});
console.log('doc coords include scroll (100+1500):', window.INK.get()[0].p[0].y);
P.fire('pointerdown',{clientX:10,clientY:10,pointerId:1,pointerType:'pen',shiftKey:true});
P.fire('pointermove',{clientX:300,clientY:14,pointerId:1,pointerType:'pen'}); flush();
P.fire('pointerup',{});
console.log('shift snaps to line:', window.INK.get()[1].tool, '| pts:', window.INK.get()[1].p.length);
tls[2].fire('click');   // box
P.fire('pointerdown',{clientX:20,clientY:20,pointerId:1,pointerType:'mouse'});
P.fire('pointermove',{clientX:200,clientY:90,pointerId:1,pointerType:'mouse'}); flush();
P.fire('pointerup',{});
console.log('box committed:', window.INK.get()[2].tool);
reg.inkpalm.fire('click');
P.fire('pointerdown',{clientX:5,clientY:5,pointerId:9,pointerType:'touch'});
console.log('touch ignored in stylus-only:', window.INK.get().length===3);
P.fire('pointerdown',{clientX:5,clientY:5,pointerId:10,pointerType:'pen'}); P.fire('pointerup',{});
console.log('pen accepted:', window.INK.get().length===4);
reg.inkundo.fire('click'); console.log('undo:', window.INK.get().length);
reg.inkredo.fire('click'); console.log('redo:', window.INK.get().length);
reg.inkclear.fire('click'); console.log('clear:', window.INK.get().length);
reg.inkredo.fire('click'); console.log('redo after clear:', window.INK.get().length);
global.docH.keydown({key:'z',ctrlKey:true,target:{tagName:'BODY'},preventDefault(){}});
console.log('ctrl+z:', window.INK.get().length);
global.docH.keydown({key:'p',target:{tagName:'TEXTAREA'}});
console.log('p ignored while typing:', window.INK.isOn()===true);
global.docH.keydown({key:'Escape',target:{tagName:'BODY'}});
console.log('escape stops pen:', window.INK.isOn()===false);
reg.inksave.fire('click'); console.log('save ran without throwing: true');
window.INK.set([{tool:'pen',color:'#000',width:3,p:[{x:1,y:1},{x:2,y:2}]}]);
console.log('INK.set:', window.INK.get().length===1);
