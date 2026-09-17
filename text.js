const fs=require('fs');
const js=fs.readFileSync('assets.py','utf8').split('JS = r"""')[1].split('"""')[0];
eval(js.split('/* ============ rendering')[0]);
const data=JSON.parse(fs.readFileSync('/tmp/all.json','utf8'));
const find=(id,i)=>data.find(p=>p.id===id).steps[i];
const cases=[
 ['q2',1,['yes','yes it is prime','prime','Yes - nothing divides it'],['no','not prime','it is composite']],
 ['q8',2,['no','No largest','there is no largest value','it can be infinitely big','no, you can keep multiplying by 7'],['yes','yes, 240']],
 ['q10',0,['odd','it is odd','2019 is odd'],['even','it is even']],
 ['q15',0,['LCM','lcm','least common multiple','I need the lcm'],['gcf','greatest common factor']],
 ['q15',3,['December 4','dec 4','4 December','12/4/2010','december 4 2010'],['December 5','November 30']],
 ['q22',0,['N+1 is divisible by all of them','it is a multiple of 2..10','N+1 divides evenly','lcm of 2 to 10'],['it is odd','prime']],
 ['g1',0,['no','not prime','No, 7 times 13','composite'],['yes','yes it is prime']],
 ['g2',1,['yes','same answer','yes, identical','Yes same primes'],['no','not the same']],
 ['g7',1,['no','no largest','nope, infinite','you can keep going forever'],['yes']],
];
let f=0;
for(const [id,i,good,bad] of cases){
  const s=find(id,i);
  for(const g of good){const r=checkAnswer(s,g); if(!r.ok){f++;console.log('SHOULD PASS',id,i,JSON.stringify(g));}}
  for(const b of bad){const r=checkAnswer(s,b); if(r.ok){f++;console.log('SHOULD FAIL',id,i,JSON.stringify(b));}}
}
// misc robustness
const q1s3=find('q1',2);
[['440 = 2^3*5*11',true],['2*2*2*5*11',true],['2^3 x 5 x 11',true],['8*55',false],['4*110',false],['440',false]].forEach(([inp,exp])=>{
  const r=checkAnswer(q1s3,inp); if(r.ok!==exp){f++;console.log('FACTOR',JSON.stringify(inp),r.ok,r.note);} else if(!exp) console.log('note for',inp,'->',r.note);
});
const q20s2=find('q20',1);
[['16 and 24',true],['16, 24',true],['24 16',true],['12 and 32',false],['16',false]].forEach(([inp,exp])=>{
  const r=checkAnswer(q20s2,inp); if(r.ok!==exp){f++;console.log('NUMS',inp,r.ok,r.note);} else if(!exp) console.log('note for',inp,'->',r.note);
});
const q6s2=find('q6',1);
[['21560',true],['21,560',true],['21560 ',true],['22000',false],['21561',false]].forEach(([inp,exp])=>{
  const r=checkAnswer(q6s2,inp); if(r.ok!==exp){f++;console.log('NUM',inp,r.ok,r.note);} else if(!exp) console.log('note for',inp,'->',r.note);
});
console.log('text/misc failures:',f);
