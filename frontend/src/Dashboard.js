import React, {useEffect, useState} from 'react';
import axios from 'axios';
export default function Dashboard(){
  const [patients,setPatients]=useState([]); const [loading,setLoading]=useState(true); const [msg,setMsg]=useState('');
  useEffect(()=>{ fetchPatients(); },[]);
  async function fetchPatients(){ try{ const res=await axios.get('/api/monitor/patients/'); setPatients(res.data);}catch(e){console.error(e);}finally{setLoading(false)}}
  async function triggerCall(id){ try{ setMsg('Triggering...'); await axios.post('/api/monitor/trigger_call/', {patient_id:id}); setMsg('Triggered'); }catch(e){console.error(e); setMsg('Failed'); } }
  return (<div>{msg && <div style={{marginBottom:12}}>{msg}</div>}{loading? <div>Loading...</div>: (<table border='1' cellPadding='8'><thead><tr><th>Patient</th><th>Phone</th><th>Active</th><th>Actions</th></tr></thead><tbody>{patients.map(p=> (<tr key={p.id}><td>{p.name}</td><td>{p.phone}</td><td>{p.active? 'Yes':'No'}</td><td><button onClick={()=>triggerCall(p.id)}>Trigger Check-in</button></td></tr>))}</tbody></table>)}</div>); }
