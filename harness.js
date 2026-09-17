const fs=require('fs');
const js=fs.readFileSync('assets.py','utf8').split('JS = r"""')[1].split('"""')[0];
// strip DOM-dependent parts: everything from "/* ============ rendering" onward
const core=js.split('/* ============ rendering')[0];
eval(core);
const data=JSON.parse(fs.readFileSync('/tmp/all.json','utf8'));
let fails=0, n=0;
function t(step,input,expect,tag){
  n++;
  const r=checkAnswer(step,input);
  if(r.ok!==expect){fails++;console.log('FAIL',tag,'|input:',JSON.stringify(input),'|got',r.ok,r.note);}
}
for(const p of data){
  p.steps.forEach((s,i)=>{
    const tag=p.id+'.s'+(i+1);
    if(s.type==='factor'){
      t(s,s.answer,true,tag);
      // expanded
      let exp=s.answer.split('*').map(tok=>{
        if(tok.includes('^')){const[b,e]=tok.split('^');return Array(+e).fill(b).join('*');}
        return tok;}).join('*');
      t(s,exp,true,tag+'-exp');
      t(s,s.answer.replace(/\*/g,' · '),true,tag+'-dot');
      const sup={'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'};
      t(s,s.answer.replace(/\^(\d)/g,(m,d)=>sup[d]).replace(/\*/g,'·'),true,tag+'-sup');
      t(s,'999',false,tag+'-wrong');
    } else if(s.type==='num'){
      t(s,String(s.answer),true,tag);
      t(s,s.answer.toLocaleString('en-US'),true,tag+'-comma');
      t(s,String(s.answer+1),false,tag+'-wrong');
    } else if(s.type==='nums'){
      t(s,s.answer.join(', '),true,tag);
      t(s,s.answer.join(' and '),true,tag+'-and');
      t(s,String(s.answer[0]),s.answer.length===1,tag+'-partial');
    } else if(s.type==='choice'){
      t(s,String(s.answer),true,tag); t(s,'('+s.answer+')',true,tag+'-paren');
      t(s,'A'===String(s.answer)?'B':'A',false,tag+'-wrong');
    } else if(s.type==='text'){
      console.log('TEXT',tag,'answer='+s.answer,'re='+JSON.stringify(s.re));
    }
  });
}
console.log('ran',n,'fails',fails);
