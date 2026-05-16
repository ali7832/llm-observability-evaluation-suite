import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, AlertTriangle, BarChart3, Brain, CheckCircle2, CircleDollarSign, Gauge, GitCompare, LineChart as LineIcon, Rocket, ShieldCheck, Sparkles } from 'lucide-react';
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import './styles.css';

const pages = ['Overview', 'Live Traces', 'Evaluation Lab', 'Regression Suite', 'Model Compare', 'Alerts', 'Release Gates'];
const qualityTrend = [{d:'Mon',quality:86,cost:42,latency:710},{d:'Tue',quality:89,cost:38,latency:640},{d:'Wed',quality:84,cost:51,latency:760},{d:'Thu',quality:92,cost:35,latency:590},{d:'Fri',quality:94,cost:33,latency:540}];
const traces = [
  ['RUN-9012','support-copilot','v12','0.91 quality','$0.014','620ms'],
  ['RUN-9022','rag-assistant','v8','0.84 quality','$0.021','780ms'],
  ['RUN-9031','sales-email','v4','0.73 quality','$0.011','520ms'],
  ['RUN-9044','claims-review','v2','0.95 quality','$0.032','940ms']
];
const comparisons = [{model:'GPT-4.1',quality:94,cost:42},{model:'Claude',quality:91,cost:38},{model:'Gemini',quality:88,cost:31},{model:'Local LLM',quality:77,cost:12}];
const alerts = ['Quality score dropped below release threshold for sales-email v4','Latency spike detected in claims-review app','Cost budget reached 84% for rag-assistant workspace'];

function fallbackEval(form){
  let quality = 0.88;
  let safety = 0.96;
  let cost = 0.018;
  let latency = 640;
  const issues = [];
  if (form.response.length < 80) { quality -= 0.16; issues.push('Response may be incomplete for the prompt intent'); }
  if (form.response.toLowerCase().includes('guarantee')) { safety -= 0.12; issues.push('Potentially risky absolute claim detected'); }
  if (form.prompt.length > 160) { cost += 0.01; latency += 140; issues.push('Long prompt increases cost and latency'); }
  return { run_id:`RUN-${Date.now().toString().slice(-5)}`, quality_score:quality, safety_score:safety, estimated_cost_usd:cost, latency_ms:latency, status: quality > 0.8 && safety > 0.9 ? 'pass' : 'review', issues: issues.length ? issues : ['Output passed quality, safety, cost, and latency checks'], evaluator_version:'eval-suite-v1.2' };
}

function App(){
  const [active,setActive] = useState('Overview');
  const [form,setForm] = useState({ app_name:'support-copilot', prompt:'Draft a concise customer support response for a billing escalation.', response:'I understand the billing issue and will escalate this to our finance specialist. We will review the duplicate charge and provide an update with next steps.' });
  const [result,setResult] = useState(fallbackEval(form));
  const metrics = useMemo(()=>[
    ['Evaluations','128K','+31%',Brain],['Quality Score','91.4%','+4.8%',ShieldCheck],['Avg Latency','620ms','-18%',Gauge],['Cost Saved','$42K','+12%',CircleDollarSign]
  ],[]);
  const evaluate = async()=>{
    try{
      const response = await fetch('/evaluate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(form)});
      if(!response.ok) throw new Error('offline');
      setResult(await response.json());
    }catch{setResult(fallbackEval(form));}
  };
  return <main className="app-shell"><aside className="sidebar"><div className="brand"><Sparkles/><div><strong>LLMOps Control</strong><span>Observability & Evaluation</span></div></div>{pages.map(p=><button className={active===p?'active':''} onClick={()=>setActive(p)} key={p}>{p}</button>)}</aside><section className="workspace"><header className="topbar"><div><p className="eyebrow">Production AI reliability</p><h1>{active}</h1></div><button onClick={evaluate}>Run evaluation</button></header>{active==='Overview'&&<Overview metrics={metrics}/>} {active==='Live Traces'&&<LiveTraces/>} {active==='Evaluation Lab'&&<EvaluationLab form={form} setForm={setForm} result={result} evaluate={evaluate}/>} {active==='Regression Suite'&&<RegressionSuite/>} {active==='Model Compare'&&<ModelCompare/>} {active==='Alerts'&&<Alerts/>} {active==='Release Gates'&&<ReleaseGates result={result}/>}</section></main>
}
function Overview({metrics}){return <><section className="metrics">{metrics.map(([l,v,d,Icon])=><article className="card" key={l}><Icon/><span>{l}</span><strong>{v}</strong><small>{d}</small></article>)}</section><section className="grid"><Panel title="Quality, cost, latency" icon={<Activity/>}><ResponsiveContainer width="100%" height={260}><LineChart data={qualityTrend}><CartesianGrid strokeDasharray="3 3" stroke="#26374a"/><XAxis dataKey="d" stroke="#9badc1"/><YAxis stroke="#9badc1"/><Tooltip/><Line dataKey="quality" stroke="#22c55e" strokeWidth={3}/><Line dataKey="cost" stroke="#f59e0b" strokeWidth={3}/></LineChart></ResponsiveContainer></Panel><Panel title="Latency trend" icon={<LineIcon/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={qualityTrend}><XAxis dataKey="d" stroke="#9badc1"/><YAxis stroke="#9badc1"/><Tooltip/><Area dataKey="latency" stroke="#38bdf8" fill="#0e7490"/></AreaChart></ResponsiveContainer></Panel></section></>}
function LiveTraces(){return <Panel title="Prompt trace stream" icon={<Activity/>}><Table rows={traces}/></Panel>}
function EvaluationLab({form,setForm,result,evaluate}){return <section className="grid"><Panel title="Prompt evaluation lab" icon={<Brain/>}>{Object.entries(form).map(([k,v])=><label key={k}>{k.replaceAll('_',' ')}<textarea value={v} onChange={e=>setForm({...form,[k]:e.target.value})}/></label>)}<button onClick={evaluate}>Evaluate output</button></Panel><Panel title="Evaluation result" icon={<CheckCircle2/>}><div className="score"><span className={result.status}>{result.status}</span><strong>{Math.round(result.quality_score*100)}%</strong><p>Safety {Math.round(result.safety_score*100)}% · ${Number(result.estimated_cost_usd).toFixed(3)} · {result.latency_ms}ms</p><small>{result.run_id} · {result.evaluator_version}</small></div>{(result.issues||[]).map(i=><div className="reason" key={i}>{i}</div>)}</Panel></section>}
function RegressionSuite(){return <section className="grid"><Panel title="Prompt regression runs" icon={<Rocket/>}><div className="reason">support-copilot v12 passed 48/50 golden tests.</div><div className="reason">rag-assistant v8 failed 2 citation faithfulness checks.</div><div className="reason">sales-email v4 requires tone and policy regression review.</div></Panel><Panel title="Regression scorecard" icon={<BarChart3/>}><ResponsiveContainer width="100%" height={260}><BarChart data={[{suite:'Support',pass:96},{suite:'RAG',pass:88},{suite:'Sales',pass:74},{suite:'Claims',pass:94}]}><XAxis dataKey="suite" stroke="#9badc1"/><YAxis stroke="#9badc1"/><Tooltip/><Bar dataKey="pass" fill="#38bdf8"/></BarChart></ResponsiveContainer></Panel></section>}
function ModelCompare(){return <Panel title="Model quality vs cost" icon={<GitCompare/>}><ResponsiveContainer width="100%" height={300}><BarChart data={comparisons}><XAxis dataKey="model" stroke="#9badc1"/><YAxis stroke="#9badc1"/><Tooltip/><Bar dataKey="quality" fill="#22c55e"/><Bar dataKey="cost" fill="#f59e0b"/></BarChart></ResponsiveContainer></Panel>}
function Alerts(){return <Panel title="Alert center" icon={<AlertTriangle/>}>{alerts.map(a=><div className="reason alert" key={a}>{a}</div>)}</Panel>}
function ReleaseGates({result}){return <section className="grid"><Panel title="Release decision" icon={<ShieldCheck/>}><div className="score"><span className={result.status}>{result.status}</span><strong>{result.status==='pass'?'Ship':'Hold'}</strong><p>Quality, safety, cost, and latency thresholds are evaluated before prompt release.</p></div></Panel><Panel title="Gate policy" icon={<Rocket/>}><div className="reason">Quality must be above 80%.</div><div className="reason">Safety must be above 90%.</div><div className="reason">Latency and cost must stay within app budget.</div></Panel></section>}
function Table({rows}){return <div className="table">{rows.map(row=><div className="row" key={row[0]}>{row.map(cell=><span key={cell}>{cell}</span>)}</div>)}</div>}
function Panel({title,icon,children}){return <article className="panel"><div className="panel-title">{icon}<h2>{title}</h2></div>{children}</article>}

createRoot(document.getElementById('root')).render(<App/>);
