import React, { useState, useEffect } from 'react';
import './App.css';

const API_URL = 'http://localhost:8000/api';

type Tab = 'basic' | 'trig' | 'fx';

function App() {
  const [tab, setTab] = useState<Tab>('basic');

  return (
    <div className="App">
      <h1>🧮 Calculator</h1>
      <div className="tabs">
        <button className={tab === 'basic' ? 'active' : ''} onClick={() => setTab('basic')}>Basic</button>
        <button className={tab === 'trig' ? 'active' : ''} onClick={() => setTab('trig')}>Trig</button>
        <button className={tab === 'fx' ? 'active' : ''} onClick={() => setTab('fx')}>FX</button>
      </div>
      <div className="tab-content">
        {tab === 'basic' && <BasicTab />}
        {tab === 'trig' && <TrigTab />}
        {tab === 'fx' && <FXTab />}
      </div>
      <footer style={{marginTop: 32, fontSize: 12, color: '#888'}}>Powered by FastAPI + React</footer>
    </div>
  );
}

function BasicTab() {
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [op, setOp] = useState<'add'|'subtract'|'multiply'|'divide'>('add');
  const [result, setResult] = useState<string>('');

  const handleCalc = async () => {
    setResult('');
    try {
      const resp = await fetch(`${API_URL}/basic`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a: Number(a), b: Number(b), op })
      });
      const data = await resp.json();
      if (resp.ok) setResult(data.result);
      else setResult(data.detail || 'Error');
    } catch (e) {
      setResult('Network error');
    }
  };

  return (
    <div className="tab-panel">
      <div className="input-row">
        <input type="number" value={a} onChange={e => setA(e.target.value)} placeholder="A" />
        <select value={op} onChange={e => setOp(e.target.value as any)}>
          <option value="add">+</option>
          <option value="subtract">-</option>
          <option value="multiply">×</option>
          <option value="divide">÷</option>
        </select>
        <input type="number" value={b} onChange={e => setB(e.target.value)} placeholder="B" />
        <button onClick={handleCalc}>Calculate</button>
      </div>
      <div className="result">{result !== '' && <>Result: <b>{result}</b></>}</div>
    </div>
  );
}

function TrigTab() {
  const [angle, setAngle] = useState('');
  const [func, setFunc] = useState<'sin'|'cos'|'tan'>('sin');
  const [degrees, setDegrees] = useState(true);
  const [result, setResult] = useState<string>('');

  const handleCalc = async () => {
    setResult('');
    try {
      const resp = await fetch(`${API_URL}/trig`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ angle: Number(angle), func, degrees })
      });
      const data = await resp.json();
      if (resp.ok) setResult(data.result);
      else setResult(data.detail || 'Error');
    } catch (e) {
      setResult('Network error');
    }
  };

  return (
    <div className="tab-panel">
      <div className="input-row">
        <select value={func} onChange={e => setFunc(e.target.value as any)}>
          <option value="sin">sin</option>
          <option value="cos">cos</option>
          <option value="tan">tan</option>
        </select>
        <input type="number" value={angle} onChange={e => setAngle(e.target.value)} placeholder="Angle" />
        <label style={{marginLeft: 8}}>
          <input type="checkbox" checked={degrees} onChange={e => setDegrees(e.target.checked)} /> Degrees
        </label>
        <button onClick={handleCalc}>Calculate</button>
      </div>
      <div className="result">{result !== '' && <>Result: <b>{result}</b></>}</div>
    </div>
  );
}

function FXTab() {
  const [amount, setAmount] = useState('');
  const [from, setFrom] = useState('USD');
  const [to, setTo] = useState('EUR');
  const [currencies, setCurrencies] = useState<string[]>([]);
  const [result, setResult] = useState<string>('');

  useEffect(() => {
    fetch(`${API_URL}/currencies`).then(r => r.json()).then(data => setCurrencies(data.currencies || []));
  }, []);

  const handleCalc = async () => {
    setResult('');
    try {
      const resp = await fetch(`${API_URL}/fx`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount: Number(amount), from_currency: from, to_currency: to })
      });
      const data = await resp.json();
      if (resp.ok) setResult(data.result);
      else setResult(data.detail || 'Error');
    } catch (e) {
      setResult('Network error');
    }
  };

  return (
    <div className="tab-panel">
      <div className="input-row">
        <input type="number" value={amount} onChange={e => setAmount(e.target.value)} placeholder="Amount" />
        <select value={from} onChange={e => setFrom(e.target.value)}>
          {currencies.map(c => <option key={c} value={c}>{c}</option>)}
        </select>
        <span style={{margin: '0 8px'}}>to</span>
        <select value={to} onChange={e => setTo(e.target.value)}>
          {currencies.map(c => <option key={c} value={c}>{c}</option>)}
        </select>
        <button onClick={handleCalc}>Convert</button>
      </div>
      <div className="result">{result !== '' && <>Result: <b>{result}</b></>}</div>
    </div>
  );
}

export default App;
