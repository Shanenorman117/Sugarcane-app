        import { useState, useEffect } from "react";

const theme = {
  bg: "#0a0f07",
  surface: "#111a0c",
  card: "#162012",
  border: "#2a3d1e",
  accent: "#5db03a",
  accentDark: "#3d7a25",
  accentGlow: "#7ed957",
  gold: "#c9a84c",
  tan: "#d4b896",
  text: "#e8f0e0",
  muted: "#7a9068",
  danger: "#e05c4a",
  warn: "#e0a84a",
  info: "#4ab0e0",
};

const css = `
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Karla:wght@400;500;600;700&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: ${theme.bg};
    color: ${theme.text};
    font-family: 'Karla', sans-serif;
    min-height: 100vh;
  }

  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: ${theme.bg}; }
  ::-webkit-scrollbar-thumb { background: ${theme.border}; border-radius: 3px; }

  .app { display: flex; height: 100vh; overflow: hidden; }

  /* SIDEBAR */
  .sidebar {
    width: 220px;
    min-width: 220px;
    background: ${theme.surface};
    border-right: 1px solid ${theme.border};
    display: flex;
    flex-direction: column;
    padding: 0;
    overflow-y: auto;
  }

  .sidebar-logo {
    padding: 20px 20px 16px;
    border-bottom: 1px solid ${theme.border};
  }
  .sidebar-logo h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem;
    color: ${theme.accentGlow};
    letter-spacing: 0.02em;
    line-height: 1.1;
  }
  .sidebar-logo span {
    font-size: 0.7rem;
    color: ${theme.muted};
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .sidebar-section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: ${theme.muted};
    padding: 16px 20px 6px;
  }

  .nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 20px;
    cursor: pointer;
    border-left: 3px solid transparent;
    font-size: 0.875rem;
    font-weight: 500;
    color: ${theme.muted};
    transition: all 0.15s;
    user-select: none;
  }
  .nav-item:hover { color: ${theme.text}; background: rgba(93,176,58,0.06); }
  .nav-item.active {
    color: ${theme.accentGlow};
    border-left-color: ${theme.accentGlow};
    background: rgba(93,176,58,0.1);
  }
  .nav-icon { font-size: 1rem; width: 20px; text-align: center; }

  /* MAIN */
  .main { flex: 1; display: flex; flex-direction: column; overflow: hidden; }

  .topbar {
    background: ${theme.surface};
    border-bottom: 1px solid ${theme.border};
    padding: 14px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
  }

  .topbar-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.25rem;
    color: ${theme.text};
  }
  .topbar-sub { font-size: 0.78rem; color: ${theme.muted}; margin-top: 1px; }

  .topbar-right { display: flex; align-items: center; gap: 12px; }

  .badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    padding: 4px 10px;
    border-radius: 20px;
    letter-spacing: 0.04em;
    font-weight: 500;
  }
  .badge-green { background: rgba(93,176,58,0.15); color: ${theme.accentGlow}; border: 1px solid rgba(93,176,58,0.3); }
  .badge-gold { background: rgba(201,168,76,0.15); color: ${theme.gold}; border: 1px solid rgba(201,168,76,0.3); }
  .badge-red { background: rgba(224,92,74,0.15); color: ${theme.danger}; border: 1px solid rgba(224,92,74,0.3); }
  .badge-blue { background: rgba(74,176,224,0.15); color: ${theme.info}; border: 1px solid rgba(74,176,224,0.3); }

  /* CONTENT */
  .content { flex: 1; overflow-y: auto; padding: 24px 28px; }

  /* CARDS */
  .card {
    background: ${theme.card};
    border: 1px solid ${theme.border};
    border-radius: 10px;
    padding: 20px;
  }
  .card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1rem;
    color: ${theme.text};
    margin-bottom: 4px;
  }
  .card-sub { font-size: 0.78rem; color: ${theme.muted}; margin-bottom: 16px; }

  /* GRID */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
  .grid-4 { display: grid; grid-template-columns: repeat(4,1fr); gap: 16px; }

  /* STAT CARD */
  .stat-card {
    background: ${theme.card};
    border: 1px solid ${theme.border};
    border-radius: 10px;
    padding: 18px 20px;
  }
  .stat-label { font-size: 0.72rem; color: ${theme.muted}; font-family: 'DM Mono', monospace; text-transform: uppercase; letter-spacing: 0.06em; }
  .stat-value { font-family: 'DM Serif Display', serif; font-size: 1.9rem; color: ${theme.text}; margin: 4px 0 2px; line-height: 1; }
  .stat-change { font-size: 0.75rem; }
  .stat-change.up { color: ${theme.accentGlow}; }
  .stat-change.down { color: ${theme.danger}; }
  .stat-change.neutral { color: ${theme.muted}; }

  /* TABLE */
  .table-wrap { overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; font-size: 0.83rem; }
  thead tr { border-bottom: 1px solid ${theme.border}; }
  th { padding: 8px 12px; text-align: left; color: ${theme.muted}; font-family: 'DM Mono', monospace; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 500; }
  td { padding: 11px 12px; border-bottom: 1px solid rgba(42,61,30,0.5); color: ${theme.text}; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: rgba(93,176,58,0.04); }

  /* PROGRESS BAR */
  .progress-bar-bg { background: rgba(42,61,30,0.8); border-radius: 4px; height: 6px; overflow: hidden; }
  .progress-bar-fill { height: 100%; border-radius: 4px; transition: width 0.3s; }
  .progress-green { background: linear-gradient(90deg, ${theme.accentDark}, ${theme.accentGlow}); }
  .progress-gold { background: linear-gradient(90deg, #a07830, ${theme.gold}); }
  .progress-red { background: ${theme.danger}; }
  .progress-blue { background: ${theme.info}; }

  /* BTN */
  .btn {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 8px 16px; border-radius: 7px; border: none;
    font-family: 'Karla', sans-serif; font-size: 0.83rem;
    font-weight: 600; cursor: pointer; transition: all 0.15s;
    letter-spacing: 0.01em;
  }
  .btn-primary { background: ${theme.accentDark}; color: #fff; }
  .btn-primary:hover { background: ${theme.accent}; }
  .btn-outline { background: transparent; color: ${theme.muted}; border: 1px solid ${theme.border}; }
  .btn-outline:hover { color: ${theme.text}; border-color: ${theme.muted}; }
  .btn-danger { background: rgba(224,92,74,0.15); color: ${theme.danger}; border: 1px solid rgba(224,92,74,0.3); }

  /* FORM */
  .form-group { margin-bottom: 14px; }
  .form-label { display: block; font-size: 0.78rem; color: ${theme.muted}; margin-bottom: 5px; font-family: 'DM Mono', monospace; letter-spacing: 0.04em; }
  .form-input, .form-select, .form-textarea {
    width: 100%; background: ${theme.surface}; border: 1px solid ${theme.border};
    color: ${theme.text}; border-radius: 7px; padding: 9px 12px;
    font-family: 'Karla', sans-serif; font-size: 0.85rem;
    outline: none; transition: border-color 0.15s;
  }
  .form-input:focus, .form-select:focus, .form-textarea:focus { border-color: ${theme.accentDark}; }
  .form-textarea { resize: vertical; min-height: 80px; }
  .form-select option { background: ${theme.surface}; }

  /* MODAL */
  .modal-overlay {
    position: fixed; inset: 0; background: rgba(0,0,0,0.7);
    display: flex; align-items: center; justify-content: center;
    z-index: 999; padding: 20px;
  }
  .modal {
    background: ${theme.card}; border: 1px solid ${theme.border};
    border-radius: 12px; padding: 24px; width: 100%; max-width: 480px;
    max-height: 90vh; overflow-y: auto;
  }
  .modal-title { font-family: 'DM Serif Display', serif; font-size: 1.15rem; color: ${theme.text}; margin-bottom: 16px; }
  .modal-footer { display: flex; gap: 10px; justify-content: flex-end; margin-top: 20px; }

  /* TIMELINE */
  .timeline { position: relative; padding-left: 24px; }
  .timeline::before { content: ''; position: absolute; left: 8px; top: 0; bottom: 0; width: 1px; background: ${theme.border}; }
  .tl-item { position: relative; margin-bottom: 20px; }
  .tl-dot { position: absolute; left: -20px; top: 4px; width: 10px; height: 10px; border-radius: 50%; background: ${theme.accentDark}; border: 2px solid ${theme.accentGlow}; }
  .tl-dot.done { background: ${theme.accentGlow}; }
  .tl-dot.warn { background: ${theme.warn}; border-color: ${theme.warn}; }
  .tl-dot.future { background: ${theme.border}; border-color: ${theme.muted}; }
  .tl-label { font-size: 0.83rem; font-weight: 600; color: ${theme.text}; }
  .tl-date { font-size: 0.72rem; color: ${theme.muted}; font-family: 'DM Mono', monospace; }
  .tl-desc { font-size: 0.8rem; color: ${theme.muted}; margin-top: 2px; }

  /* PHASE PILL */
  .phase-pill {
    display: inline-block; padding: 3px 10px; border-radius: 20px;
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.03em;
  }
  .pill-prep { background: rgba(201,168,76,0.15); color: ${theme.gold}; }
  .pill-plant { background: rgba(93,176,58,0.15); color: ${theme.accentGlow}; }
  .pill-maintain { background: rgba(74,176,224,0.15); color: ${theme.info}; }
  .pill-harvest { background: rgba(224,92,74,0.15); color: ${theme.danger}; }
  .pill-fallow { background: rgba(122,144,104,0.15); color: ${theme.muted}; }

  /* WEATHER BAR */
  .weather-bar {
    background: rgba(93,176,58,0.06); border: 1px solid ${theme.border};
    border-radius: 8px; padding: 12px 16px;
    display: flex; gap: 24px; align-items: center;
    margin-bottom: 20px; flex-wrap: wrap;
  }
  .weather-item { display: flex; flex-direction: column; align-items: center; gap: 2px; }
  .weather-val { font-family: 'DM Serif Display', serif; font-size: 1.1rem; color: ${theme.text}; }
  .weather-lbl { font-size: 0.65rem; color: ${theme.muted}; font-family: 'DM Mono', monospace; text-transform: uppercase; letter-spacing: 0.06em; }

  /* ALERT */
  .alert { border-radius: 8px; padding: 10px 14px; font-size: 0.82rem; margin-bottom: 10px; display: flex; gap: 10px; align-items: flex-start; }
  .alert-warn { background: rgba(224,168,74,0.1); border: 1px solid rgba(224,168,74,0.3); color: ${theme.warn}; }
  .alert-danger { background: rgba(224,92,74,0.1); border: 1px solid rgba(224,92,74,0.3); color: ${theme.danger}; }
  .alert-success { background: rgba(93,176,58,0.1); border: 1px solid rgba(93,176,58,0.3); color: ${theme.accentGlow}; }
  .alert-info { background: rgba(74,176,224,0.1); border: 1px solid rgba(74,176,224,0.3); color: ${theme.info}; }

  /* SECTION HEADER */
  .section-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
  .section-title { font-family: 'DM Serif Display', serif; font-size: 1.05rem; color: ${theme.text}; }

  /* ROW FLEX */
  .row { display: flex; gap: 16px; margin-bottom: 16px; flex-wrap: wrap; }
  .row > * { flex: 1; min-width: 0; }

  .mb8 { margin-bottom: 8px; }
  .mb16 { margin-bottom: 16px; }
  .mb24 { margin-bottom: 24px; }

  .text-muted { color: ${theme.muted}; }
  .text-accent { color: ${theme.accentGlow}; }
  .text-gold { color: ${theme.gold}; }
  .text-danger { color: ${theme.danger}; }
  .text-sm { font-size: 0.78rem; }
  .font-mono { font-family: 'DM Mono', monospace; }
  .bold { font-weight: 700; }

  .divider { border: none; border-top: 1px solid ${theme.border}; margin: 16px 0; }
`;

// ─── DATA ───────────────────────────────────────────────────────────────────

const INITIAL_FIELDS = [
  { id: 1, name: "Block A – North", area: 45, variety: "NCo 376", phase: "maintain", plantDate: "2024-03-10", nextHarvest: "2025-09-10", ratoon: 2, soilType: "Loam", irrigated: true, notes: "Good stand, monitor for borer" },
  { id: 2, name: "Block B – South", area: 30, variety: "CP 72-2086", phase: "harvest", plantDate: "2023-11-05", nextHarvest: "2025-05-05", ratoon: 3, soilType: "Clay-Loam", irrigated: true, notes: "Ready for harvest — TCH ~85t" },
  { id: 3, name: "Block C – East", area: 20, variety: "NCo 376", phase: "prep", plantDate: null, nextHarvest: null, ratoon: 0, soilType: "Sandy-Loam", irrigated: false, notes: "Sub-soiling in progress" },
  { id: 4, name: "Block D – West", area: 38, variety: "Q208", phase: "plant", plantDate: "2025-02-15", nextHarvest: "2026-08-15", ratoon: 1, soilType: "Loam", irrigated: true, notes: "Newly planted plant crop" },
  { id: 5, name: "Block E – Central", area: 25, variety: "CP 72-2086", phase: "fallow", plantDate: null, nextHarvest: null, ratoon: 0, soilType: "Clay", irrigated: false, notes: "Fallow – green manure crop sown" },
];

const INITIAL_TASKS = [
  { id: 1, fieldId: 1, type: "Fertilisation", date: "2025-04-25", status: "pending", notes: "Top dressing — 200 kg/ha Urea", assignee: "Team A" },
  { id: 2, fieldId: 2, type: "Harvest", date: "2025-05-01", status: "pending", notes: "Mechanical harvest — Block B", assignee: "Harvest Crew" },
  { id: 3, fieldId: 3, type: "Subsoiling", date: "2025-04-20", status: "done", notes: "Deep rip to 60cm complete", assignee: "Team B" },
  { id: 4, fieldId: 4, type: "Irrigation", date: "2025-04-18", status: "done", notes: "Drip irrigation cycle 3", assignee: "Irrigation" },
  { id: 5, fieldId: 1, type: "Pest Scouting", date: "2025-04-22", status: "pending", notes: "Check for stalk borer damage", assignee: "Scout A" },
  { id: 6, fieldId: 3, type: "Liming", date: "2025-04-30", status: "pending", notes: "Apply 2t/ha dolomitic lime", assignee: "Team B" },
  { id: 7, fieldId: 5, type: "Weed Control", date: "2025-04-19", status: "done", notes: "Herbicide application complete", assignee: "Team C" },
];

const INITIAL_INPUTS = [
  { id: 1, name: "Urea (46% N)", category: "Fertiliser", unit: "bags (50kg)", qty: 420, minQty: 100, unitCost: 92000 },
  { id: 2, name: "DAP (18-46-0)", category: "Fertiliser", unit: "bags (50kg)", qty: 180, minQty: 50, unitCost: 115000 },
  { id: 3, name: "KCl Muriate of Potash", category: "Fertiliser", unit: "bags (50kg)", qty: 95, minQty: 50, unitCost: 105000 },
  { id: 4, name: "Atrazine 500SC", category: "Herbicide", unit: "litres", qty: 38, minQty: 20, unitCost: 45000 },
  { id: 5, name: "Carbofuran 5G", category: "Pesticide", unit: "kg", qty: 12, minQty: 20, unitCost: 28000 },
  { id: 6, name: "Glyphosate 480SL", category: "Herbicide", unit: "litres", qty: 55, minQty: 25, unitCost: 32000 },
  { id: 7, name: "NCo 376 Seed Cane", category: "Seed Cane", unit: "tonnes", qty: 4, minQty: 10, unitCost: 380000 },
];

const PREP_STAGES = [
  { label: "Site Assessment & Soil Analysis", desc: "Soil sampling, pH test, drainage evaluation", status: "done" },
  { label: "Land Clearing", desc: "Remove existing crop residues, stumps, trees", status: "done" },
  { label: "Deep Sub-soiling / Ripping", desc: "Break hardpan at 50–70 cm depth", status: "done" },
  { label: "Primary Tillage (Ploughing)", desc: "Mouldboard or disc plough 30–40 cm", status: "current" },
  { label: "Liming & Soil Amendments", desc: "Adjust pH, apply gypsum if needed", status: "pending" },
  { label: "Secondary Tillage (Harrowing)", desc: "Break clods, level surface", status: "pending" },
  { label: "Drainage & Road Construction", desc: "Grade drains, internal roads", status: "pending" },
  { label: "Furrow Making / Row Marking", desc: "Mark rows at 1.5–1.8 m spacing", status: "pending" },
];

const phaseLabel = { prep: "Land Prep", plant: "Planting", maintain: "Maintenance", harvest: "Harvest", fallow: "Fallow" };
const phaseClass = { prep: "pill-prep", plant: "pill-plant", maintain: "pill-maintain", harvest: "pill-harvest", fallow: "pill-fallow" };

// ─── APP ─────────────────────────────────────────────────────────────────────

export default function App() {
  const [page, setPage] = useState("dashboard");
  const [fields, setFields] = useState(INITIAL_FIELDS);
  const [tasks, setTasks] = useState(INITIAL_TASKS);
  const [inputs, setInputs] = useState(INITIAL_INPUTS);
  const [modal, setModal] = useState(null);
  const [form, setForm] = useState({});
  const [editId, setEditId] = useState(null);

  const totalArea = fields.reduce((a, f) => a + f.area, 0);
  const pendingTasks = tasks.filter(t => t.status === "pending").length;
  const lowStock = inputs.filter(i => i.qty < i.minQty).length;
  const harvestReady = fields.filter(f => f.phase === "harvest").length;

  const openModal = (type, id = null) => {
    setModal(type);
    setEditId(id);
    if (id && type === "editField") {
      setForm({ ...fields.find(f => f.id === id) });
    } else if (id && type === "editTask") {
      setForm({ ...tasks.find(t => t.id === id) });
    } else {
      setForm({});
    }
  };
  const closeModal = () => { setModal(null); setForm({}); setEditId(null); };

  const saveField = () => {
    if (editId) {
      setFields(fields.map(f => f.id === editId ? { ...f, ...form } : f));
    } else {
      setFields([...fields, { id: Date.now(), ...form, area: Number(form.area) || 0 }]);
    }
    closeModal();
  };

  const saveTask = () => {
    if (editId) {
      setTasks(tasks.map(t => t.id === editId ? { ...t, ...form } : t));
    } else {
      setTasks([...tasks, { id: Date.now(), ...form, fieldId: Number(form.fieldId) }]);
    }
    closeModal();
  };

  const toggleTask = (id) => {
    setTasks(tasks.map(t => t.id === id ? { ...t, status: t.status === "done" ? "pending" : "done" } : t));
  };

  const deleteField = (id) => setFields(fields.filter(f => f.id !== id));
  const deleteTask = (id) => setTasks(tasks.filter(t => t.id !== id));

  const adjustStock = (id, delta) => {
    setInputs(inputs.map(i => i.id === id ? { ...i, qty: Math.max(0, i.qty + delta) } : i));
  };

  return (
    <>
      <style>{css}</style>
      <div className="app">
        <Sidebar page={page} setPage={setPage} pendingTasks={pendingTasks} lowStock={lowStock} />
        <div className="main">
          <Topbar page={page} harvestReady={harvestReady} pendingTasks={pendingTasks} />
          <div className="content">
            {page === "dashboard" && <Dashboard fields={fields} tasks={tasks} inputs={inputs} totalArea={totalArea} pendingTasks={pendingTasks} lowStock={lowStock} harvestReady={harvestReady} setPage={setPage} />}
            {page === "fields" && <Fields fields={fields} tasks={tasks} openModal={openModal} deleteField={deleteField} />}
            {page === "landprep" && <LandPrep fields={fields} />}
            {page === "planting" && <Planting fields={fields} />}
            {page === "maintenance" && <Maintenance fields={fields} tasks={tasks} toggleTask={toggleTask} openModal={openModal} deleteTask={deleteTask} />}
            {page === "harvest" && <Harvest fields={fields} />}
            {page === "tasks" && <Tasks tasks={tasks} fields={fields} toggleTask={toggleTask} openModal={openModal} deleteTask={deleteTask} />}
            {page === "inventory" && <Inventory inputs={inputs} adjustStock={adjustStock} />}
          </div>
        </div>
      </div>
      {modal === "addField" && <FieldModal form={form} setForm={setForm} onSave={saveField} onClose={closeModal} isEdit={false} />}
      {modal === "editField" && <FieldModal form={form} setForm={setForm} onSave={saveField} onClose={closeModal} isEdit={true} />}
      {modal === "addTask" && <TaskModal form={form} setForm={setForm} fields={fields} onSave={saveTask} onClose={closeModal} isEdit={false} />}
      {modal === "editTask" && <TaskModal form={form} setForm={setForm} fields={fields} onSave={saveTask} onClose={closeModal} isEdit={true} />}
    </>
  );
}

// ─── SIDEBAR ─────────────────────────────────────────────────────────────────

const navItems = [
  { id: "dashboard", icon: "🌿", label: "Overview" },
  { id: "fields", icon: "🗺️", label: "Field Registry" },
  { id: "landprep", icon: "🚜", label: "Land Preparation" },
  { id: "planting", icon: "🌱", label: "Planting" },
  { id: "maintenance", icon: "🔧", label: "Maintenance" },
  { id: "harvest", icon: "⚙️", label: "Harvest" },
  { id: "tasks", icon: "📋", label: "Task Schedule" },
  { id: "inventory", icon: "📦", label: "Input Inventory" },
];

function Sidebar({ page, setPage, pendingTasks, lowStock }) {
  return (
    <div className="sidebar">
      <div className="sidebar-logo">
        <h1>🌾 CaneEstate</h1>
        <span>Estate Manager v1.0</span>
      </div>
      <div className="sidebar-section-label">Navigation</div>
      {navItems.map(n => (
        <div key={n.id} className={`nav-item${page === n.id ? " active" : ""}`} onClick={() => setPage(n.id)}>
          <span className="nav-icon">{n.icon}</span>
          <span>{n.label}</span>
          {n.id === "tasks" && pendingTasks > 0 && <span style={{ marginLeft: "auto", background: theme.accentDark, color: "#fff", borderRadius: "10px", fontSize: "0.65rem", padding: "1px 7px" }}>{pendingTasks}</span>}
          {n.id === "inventory" && lowStock > 0 && <span style={{ marginLeft: "auto", background: theme.danger, color: "#fff", borderRadius: "10px", fontSize: "0.65rem", padding: "1px 7px" }}>{lowStock}</span>}
        </div>
      ))}
      <div style={{ marginTop: "auto", padding: "16px 20px", borderTop: `1px solid ${theme.border}` }}>
        <div style={{ fontSize: "0.72rem", color: theme.muted, fontFamily: "'DM Mono', monospace" }}>
          Season: 2024/2025<br />
          <span style={{ color: theme.accentGlow }}>● Active</span>
        </div>
      </div>
    </div>
  );
}

// ─── TOPBAR ──────────────────────────────────────────────────────────────────

const pageTitles = {
  dashboard: ["Estate Overview", "Season 2024/2025"],
  fields: ["Field Registry", "Manage all blocks and plots"],
  landprep: ["Land Preparation", "Tillage, drainage & soil conditioning"],
  planting: ["Planting Programme", "Variety selection, spacing & planting guide"],
  maintenance: ["Maintenance", "Fertilisation, irrigation, pest & disease"],
  harvest: ["Harvest Management", "Scheduling, yield tracking & logistics"],
  tasks: ["Task Schedule", "All pending and completed activities"],
  inventory: ["Input Inventory", "Fertilisers, chemicals & seed cane"],
};

function Topbar({ page, harvestReady, pendingTasks }) {
  const [title, sub] = pageTitles[page] || ["", ""];
  const today = new Date().toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
  return (
    <div className="topbar">
      <div>
        <div className="topbar-title">{title}</div>
        <div className="topbar-sub">{sub}</div>
      </div>
      <div className="topbar-right">
        {harvestReady > 0 && <span className="badge badge-red">🔴 {harvestReady} Ready to Harvest</span>}
        {pendingTasks > 0 && <span className="badge badge-gold">📋 {pendingTasks} Pending</span>}
        <span className="badge badge-green">📅 {today}</span>
      </div>
    </div>
  );
}

// ─── DASHBOARD ───────────────────────────────────────────────────────────────

function Dashboard({ fields, tasks, inputs, totalArea, pendingTasks, lowStock, harvestReady, setPage }) {
  const phaseCount = { prep: 0, plant: 0, maintain: 0, harvest: 0, fallow: 0 };
  fields.forEach(f => { if (phaseCount[f.phase] !== undefined) phaseCount[f.phase]++; });
  const recentTasks = [...tasks].sort((a, b) => a.date.localeCompare(b.date)).slice(0, 5);

  return (
    <>
      {/* Weather-like summary bar */}
      <div className="weather-bar">
        <div style={{ marginRight: 8 }}>
          <div style={{ fontSize: "0.65rem", color: theme.muted, fontFamily: "'DM Mono', monospace", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 2 }}>Estate Status</div>
          <div style={{ fontFamily: "'DM Serif Display', serif", fontSize: "1rem", color: theme.accentGlow }}>🌾 Season Active</div>
        </div>
        {[
          { val: totalArea + " ha", lbl: "Total Area" },
          { val: fields.length, lbl: "Blocks" },
          { val: phaseCount.maintain + phaseCount.plant, lbl: "Growing" },
          { val: harvestReady, lbl: "Harvest Ready" },
          { val: pendingTasks, lbl: "Tasks Due" },
          { val: lowStock, lbl: "Low Stock" },
        ].map(w => (
          <div className="weather-item" key={w.lbl}>
            <div className="weather-val">{w.val}</div>
            <div className="weather-lbl">{w.lbl}</div>
          </div>
        ))}
      </div>

      {/* Alerts */}
      {lowStock > 0 && <div className="alert alert-warn mb8">⚠️ <span><strong>{lowStock} input(s)</strong> are below minimum stock levels.</span></div>}
      {harvestReady > 0 && <div className="alert alert-danger mb8">🔴 <span><strong>{harvestReady} block(s)</strong> are ready for harvest. Schedule cutting crews.</span></div>}
      <div className="alert alert-success mb16">✅ <span>Subsoiling on Block C completed. Primary tillage scheduled for 2025-04-25.</span></div>

      {/* Stat cards */}
      <div className="grid-4 mb16">
        <div className="stat-card">
          <div className="stat-label">Total Area</div>
          <div className="stat-value">{totalArea}</div>
          <div className="stat-change neutral">hectares managed</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Est. Yield (TCH)</div>
          <div className="stat-value">~82</div>
          <div className="stat-change up">▲ +4 t/ha vs last season</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Pending Tasks</div>
          <div className="stat-value">{pendingTasks}</div>
          <div className="stat-change neutral">activities due</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Input Items</div>
          <div className="stat-value">{inputs.length}</div>
          <div className="stat-change down">{lowStock > 0 ? `▼ ${lowStock} below minimum` : "✓ All stocked"}</div>
        </div>
      </div>

      <div className="grid-2 mb16">
        {/* Phase breakdown */}
        <div className="card">
          <div className="card-title">Field Phase Breakdown</div>
          <div className="card-sub">Current status of all estate blocks</div>
          {Object.entries(phaseCount).map(([ph, cnt]) => (
            <div key={ph} style={{ marginBottom: 12 }}>
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4 }}>
                <span className={`phase-pill ${phaseClass[ph]}`}>{phaseLabel[ph]}</span>
                <span className="text-sm text-muted font-mono">{cnt} block{cnt !== 1 ? "s" : ""}</span>
              </div>
              <div className="progress-bar-bg">
                <div className={`progress-bar-fill ${ph === "harvest" ? "progress-red" : ph === "maintain" ? "progress-green" : ph === "plant" ? "progress-blue" : "progress-gold"}`}
                  style={{ width: `${(cnt / fields.length) * 100}%` }} />
              </div>
            </div>
          ))}
        </div>

        {/* Upcoming tasks */}
        <div className="card">
          <div className="section-header">
            <div className="card-title">Upcoming Tasks</div>
            <button className="btn btn-outline" style={{ fontSize: "0.75rem", padding: "5px 10px" }} onClick={() => setPage("tasks")}>View All</button>
          </div>
          {recentTasks.map(t => {
            const field = fields.find(f => f.id === t.fieldId);
            return (
              <div key={t.id} style={{ display: "flex", gap: 10, alignItems: "center", marginBottom: 10, opacity: t.status === "done" ? 0.5 : 1 }}>
                <div style={{ fontSize: "1.1rem" }}>{t.status === "done" ? "✅" : "⏳"}</div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontSize: "0.83rem", fontWeight: 600 }}>{t.type}</div>
                  <div style={{ fontSize: "0.72rem", color: theme.muted }}>{field?.name} · {t.date}</div>
                </div>
                <span className={`badge ${t.status === "done" ? "badge-green" : "badge-gold"}`}>{t.status}</span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Fields mini-table */}
      <div className="card">
        <div className="section-header">
          <div className="card-title">Estate Field Summary</div>
          <button className="btn btn-outline" style={{ fontSize: "0.75rem", padding: "5px 10px" }} onClick={() => setPage("fields")}>Manage Fields</button>
        </div>
        <div className="table-wrap">
          <table>
            <thead><tr><th>Block</th><th>Area (ha)</th><th>Variety</th><th>Phase</th><th>Ratoon</th><th>Next Harvest</th></tr></thead>
            <tbody>
              {fields.map(f => (
                <tr key={f.id}>
                  <td className="bold">{f.name}</td>
                  <td>{f.area}</td>
                  <td className="font-mono" style={{ fontSize: "0.78rem" }}>{f.variety}</td>
                  <td><span className={`phase-pill ${phaseClass[f.phase]}`}>{phaseLabel[f.phase]}</span></td>
                  <td>{f.ratoon === 0 ? "—" : `R${f.ratoon}`}</td>
                  <td className="text-muted">{f.nextHarvest || "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

// ─── FIELDS ──────────────────────────────────────────────────────────────────

function Fields({ fields, tasks, openModal, deleteField }) {
  return (
    <>
      <div className="section-header mb16">
        <div className="section-title">Field Registry ({fields.length} blocks, {fields.reduce((a, f) => a + f.area, 0)} ha total)</div>
        <button className="btn btn-primary" onClick={() => openModal("addField")}>＋ Add Block</button>
      </div>
      <div className="grid-2">
        {fields.map(f => {
          const blockTasks = tasks.filter(t => t.fieldId === f.id && t.status === "pending");
          return (
            <div className="card" key={f.id}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 10 }}>
                <div>
                  <div style={{ fontFamily: "'DM Serif Display', serif", fontSize: "1rem" }}>{f.name}</div>
                  <div style={{ fontSize: "0.72rem", color: theme.muted, fontFamily: "'DM Mono', monospace" }}>{f.area} ha · {f.soilType} · {f.irrigated ? "Irrigated" : "Dryland"}</div>
                </div>
                <span className={`phase-pill ${phaseClass[f.phase]}`}>{phaseLabel[f.phase]}</span>
              </div>
              <div className="grid-2 mb8" style={{ gap: 8 }}>
                {[
                  ["Variety", f.variety],
                  ["Ratoon", f.ratoon === 0 ? "Plant Crop" : `Ratoon ${f.ratoon}`],
                  ["Planted", f.plantDate || "—"],
                  ["Harvest ETA", f.nextHarvest || "—"],
                ].map(([l, v]) => (
                  <div key={l} style={{ background: theme.surface, borderRadius: 6, padding: "7px 10px" }}>
                    <div style={{ fontSize: "0.65rem", color: theme.muted, fontFamily: "'DM Mono', monospace", textTransform: "uppercase", letterSpacing: "0.06em" }}>{l}</div>
                    <div style={{ fontSize: "0.83rem", marginTop: 1 }}>{v}</div>
                  </div>
                ))}
              </div>
              {f.notes && <div style={{ fontSize: "0.78rem", color: theme.muted, marginBottom: 10 }}>💬 {f.notes}</div>}
              {blockTasks.length > 0 && <div className="alert alert-info" style={{ marginBottom: 10, padding: "6px 10px" }}>📋 {blockTasks.length} pending task(s)</div>}
              <div style={{ display: "flex", gap: 8, marginTop: 8 }}>
                <button className="btn btn-outline" style={{ flex: 1, justifyContent: "center" }} onClick={() => openModal("editField", f.id)}>✏️ Edit</button>
                <button className="btn btn-danger" onClick={() => { if (confirm(`Delete ${f.name}?`)) deleteField(f.id); }}>🗑️</button>
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
}

// ─── LAND PREP ───────────────────────────────────────────────────────────────

function LandPrep({ fields }) {
  const prepFields = fields.filter(f => f.phase === "prep");
  return (
    <>
      <div className="alert alert-info mb16">📘 Land preparation is the foundation of a productive sugarcane crop. Proper tillage, drainage and soil conditioning significantly impact stand establishment and long-term yields.</div>
      <div className="grid-2 mb16">
        <div className="card">
          <div className="card-title">Preparation Stages</div>
          <div className="card-sub">Standard workflow for new land or replanting</div>
          <div className="timeline">
            {PREP_STAGES.map((s, i) => (
              <div className="tl-item" key={i}>
                <div className={`tl-dot ${s.status === "done" ? "done" : s.status === "current" ? "" : "future"}`} />
                <div className="tl-label">{i + 1}. {s.label} {s.status === "done" ? "✅" : s.status === "current" ? "🔄" : ""}</div>
                <div className="tl-desc">{s.desc}</div>
              </div>
            ))}
          </div>
        </div>
        <div>
          <div className="card mb16">
            <div className="card-title">Soil Requirements</div>
            <div className="card-sub">Optimal parameters for sugarcane</div>
            {[
              ["Soil pH", "5.5 – 6.5", "Adjust with lime or sulphur"],
              ["Organic Matter", "> 2.5%", "Incorporate trash / green manure"],
              ["Drainage", "< 50 cm water table", "Install drains if needed"],
              ["Tillage Depth", "40 – 60 cm", "Break compaction layers"],
              ["Row Spacing", "1.5 – 1.8 m", "Standard for mechanised ops"],
              ["Slope", "< 8%", "Terrace or contour-plough on slopes"],
            ].map(([label, val, note]) => (
              <div key={label} style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", padding: "8px 0", borderBottom: `1px solid ${theme.border}` }}>
                <span style={{ fontSize: "0.82rem", color: theme.muted }}>{label}</span>
                <div style={{ textAlign: "right" }}>
                  <div style={{ fontSize: "0.83rem", fontWeight: 600, color: theme.accentGlow }}>{val}</div>
                  <div style={{ fontSize: "0.7rem", color: theme.muted }}>{note}</div>
                </div>
              </div>
            ))}
          </div>
          <div className="card">
            <div className="card-title">Blocks in Preparation</div>
            <div className="card-sub">Currently being readied for planting</div>
            {prepFields.length === 0 ? <div className="text-muted text-sm">No blocks currently in land preparation.</div> :
              prepFields.map(f => (
                <div key={f.id} style={{ display: "flex", justifyContent: "space-between", padding: "8px 0", borderBottom: `1px solid ${theme.border}` }}>
                  <div>
                    <div style={{ fontWeight: 600, fontSize: "0.85rem" }}>{f.name}</div>
                    <div style={{ fontSize: "0.72rem", color: theme.muted }}>{f.area} ha · {f.soilType}</div>
                  </div>
                  <div style={{ fontSize: "0.75rem", color: theme.muted }}>{f.notes}</div>
                </div>
              ))
            }
          </div>
        </div>
      </div>
      <div className="card">
        <div className="card-title">Equipment Checklist</div>
        <div className="card-sub">Typical machinery requirements for land preparation</div>
        <div className="grid-3" style={{ gap: 10, marginTop: 4 }}>
          {[
            ["🚜", "Sub-soiler / Ripper", "Heavy-duty 3–5 tine, 50–70 cm depth"],
            ["🔄", "Mouldboard Plough", "Primary tillage, 30–40 cm"],
            ["⚙️", "Disc Harrow", "Secondary tillage, clod breaking"],
            ["📏", "Ridger / Furrower", "Forming planting furrows"],
            ["🌊", "Grader / Excavator", "Drain construction"],
            ["🌿", "Spray Rig", "Pre-plant herbicide application"],
          ].map(([icon, name, desc]) => (
            <div key={name} style={{ background: theme.surface, borderRadius: 8, padding: "12px 14px" }}>
              <div style={{ fontSize: "1.4rem", marginBottom: 4 }}>{icon}</div>
              <div style={{ fontWeight: 600, fontSize: "0.83rem" }}>{name}</div>
              <div style={{ fontSize: "0.72rem", color: theme.muted, marginTop: 2 }}>{desc}</div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

// ─── PLANTING ────────────────────────────────────────────────────────────────

function Planting({ fields }) {
  const plantFields = fields.filter(f => f.phase === "plant");
  return (
    <>
      <div className="grid-2 mb16">
        <div className="card">
          <div className="card-title">Planting Calendar</div>
          <div className="card-sub">Recommended planting windows</div>
          {[
            { season: "Main Season", window: "Oct – Dec", notes: "Primary planting; best establishment", recommended: true },
            { season: "Spring Planting", window: "Feb – Mar", notes: "Good for tropical areas", recommended: true },
            { season: "Off-Season", window: "Jun – Aug", notes: "Possible with irrigation; higher risk", recommended: false },
          ].map(s => (
            <div key={s.season} style={{ background: theme.surface, borderRadius: 8, padding: "12px 14px", marginBottom: 10, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <div>
                <div style={{ fontWeight: 600, fontSize: "0.85rem" }}>{s.season}</div>
                <div style={{ fontSize: "0.72rem", color: theme.muted }}>{s.notes}</div>
              </div>
              <div style={{ textAlign: "right" }}>
                <div style={{ fontFamily: "'DM Mono', monospace", fontSize: "0.82rem", color: theme.gold }}>{s.window}</div>
                <span className={`badge ${s.recommended ? "badge-green" : "badge-gold"}`} style={{ fontSize: "0.65rem", marginTop: 2, display: "inline-block" }}>{s.recommended ? "Recommended" : "Possible"}</span>
              </div>
            </div>
          ))}
        </div>
        <div className="card">
          <div className="card-title">Variety Guide</div>
          <div className="card-sub">Common varieties and key characteristics</div>
          <div className="table-wrap">
            <table>
              <thead><tr><th>Variety</th><th>Maturity</th><th>TCH</th><th>CCS</th><th>Notes</th></tr></thead>
              <tbody>
                {[
                  ["NCo 376", "Late", "85–100", "14–15", "High yield, borer susceptible"],
                  ["CP 72-2086", "Mid", "80–95", "13–14", "Good ratoon vigour"],
                  ["Q208", "Mid-late", "90–110", "14–16", "Excellent sugar content"],
                  ["SP 80-3280", "Early", "75–90", "12–14", "Drought tolerant"],
                  ["RB 85-5536", "Mid", "85–100", "13–15", "Strong tillering"],
                ].map(r => <tr key={r[0]}><td className="bold font-mono" style={{ fontSize: "0.78rem" }}>{r[0]}</td><td>{r[1]}</td><td style={{ color: theme.accentGlow }}>{r[2]}</td><td style={{ color: theme.gold }}>{r[3]}</td><td style={{ color: theme.muted, fontSize: "0.75rem" }}>{r[4]}</td></tr>)}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div className="grid-3 mb16">
        {[
          { title: "Seed Rate", val: "8–10 t/ha", desc: "2–3 bud setts, end-to-end in furrow", icon: "🌱" },
          { title: "Planting Depth", val: "20–25 cm", desc: "Furrow depth for optimal germination", icon: "📐" },
          { title: "Row Spacing", val: "1.5–1.8 m", desc: "Standard wide-row for mechanisation", icon: "📏" },
          { title: "Seed Cane Age", val: "8–10 months", desc: "Fresh, healthy billets preferred", icon: "🎋" },
          { title: "Fertiliser at Plant", val: "200 kg/ha DAP", desc: "Starter P + N in furrow", icon: "💊" },
          { title: "Germination", val: "28–35 days", desc: "Expect 75–85% shoot emergence", icon: "⏱️" },
        ].map(c => (
          <div key={c.title} className="card" style={{ display: "flex", gap: 12, alignItems: "flex-start" }}>
            <div style={{ fontSize: "1.5rem" }}>{c.icon}</div>
            <div>
              <div style={{ fontFamily: "'DM Mono', monospace", fontSize: "0.65rem", color: theme.muted, textTransform: "uppercase", letterSpacing: "0.06em" }}>{c.title}</div>
              <div style={{ fontFamily: "'DM Serif Display', serif", fontSize: "1.1rem", color: theme.accentGlow, margin: "2px 0" }}>{c.val}</div>
              <div style={{ fontSize: "0.72rem", color: theme.muted }}>{c.desc}</div>
            </div>
          </div>
        ))}
      </div>
      <div className="card">
        <div className="card-title">Currently Planting</div>
        <div className="card-sub">Blocks in active planting phase</div>
        {plantFields.length === 0 ? <div className="text-muted text-sm">No blocks currently in planting phase.</div> :
          <div className="table-wrap">
            <table>
              <thead><tr><th>Block</th><th>Area</th><th>Variety</th><th>Plant Date</th><th>Expected Harvest</th><th>Notes</th></tr></thead>
              <tbody>
                {plantFields.map(f => <tr key={f.id}><td className="bold">{f.name}</td><td>{f.area} ha</td><td className="font-mono" style={{ fontSize: "0.78rem" }}>{f.variety}</td><td>{f.plantDate}</td><td className="text-accent">{f.nextHarvest}</td><td className="text-muted text-sm">{f.notes}</td></tr>)}
              </tbody>
            </table>
          </div>
        }
      </div>
    </>
  );
}

// ─── MAINTENANCE ─────────────────────────────────────────────────────────────

function Maintenance({ fields, tasks, toggleTask, openModal, deleteTask }) {
  const maintTasks = tasks.filter(t => ["Fertilisation", "Irrigation", "Pest Scouting", "Weed Control", "Fungicide", "Trashing"].includes(t.type));
  return (
    <>
      <div className="grid-3 mb16">
        {[
          { icon: "💊", title: "Fertilisation", desc: "NPK programme: Split applications at planting, 3 & 6 months", color: theme.gold },
          { icon: "💧", title: "Irrigation", desc: "Furrow, drip or overhead. Critical: germination & grand growth", color: theme.info },
          { icon: "🐛", title: "Pest & Disease", desc: "Monitor for stalk borer, aphids, smut, ratoon stunting", color: theme.danger },
          { icon: "🌿", title: "Weed Control", desc: "Pre-emergence Atrazine; inter-row cultivation at 8–12 weeks", color: theme.accentGlow },
          { icon: "🍃", title: "Trashing", desc: "Remove dead leaves to reduce pest habitat & disease spread", color: theme.tan },
          { icon: "📈", title: "Growth Monitoring", desc: "Monthly stalk counts, height & Brix measurements", color: theme.muted },
        ].map(c => (
          <div className="card" key={c.title} style={{ borderLeft: `3px solid ${c.color}` }}>
            <div style={{ fontSize: "1.4rem", marginBottom: 6 }}>{c.icon}</div>
            <div style={{ fontWeight: 700, marginBottom: 4 }}>{c.title}</div>
            <div style={{ fontSize: "0.78rem", color: theme.muted }}>{c.desc}</div>
          </div>
        ))}
      </div>
      <div className="grid-2 mb16">
        <div className="card">
          <div className="card-title">NPK Fertiliser Schedule</div>
          <div className="card-sub">Typical programme per hectare</div>
          <div className="table-wrap">
            <table>
              <thead><tr><th>Stage</th><th>Time</th><th>N (kg)</th><th>P (kg)</th><th>K (kg)</th></tr></thead>
              <tbody>
                {[
                  ["Basal", "At planting", "30", "60", "60"],
                  ["1st Top", "6–8 wks", "80", "—", "60"],
                  ["2nd Top", "4–5 mths", "90", "—", "80"],
                  ["Ratoon Basal", "After harvest", "40", "40", "60"],
                  ["Ratoon Top", "8 wks post-harvest", "100", "—", "80"],
                ].map(r => <tr key={r[0]}><td className="bold">{r[0]}</td><td>{r[1]}</td><td style={{ color: theme.accentGlow }}>{r[2]}</td><td style={{ color: theme.gold }}>{r[3]}</td><td style={{ color: theme.info }}>{r[4]}</td></tr>)}
              </tbody>
            </table>
          </div>
        </div>
        <div className="card">
          <div className="card-title">Key Pests & Diseases</div>
          <div className="card-sub">Identification and action thresholds</div>
          {[
            { name: "Eldana Stalk Borer", type: "Pest", threshold: "> 2% infestation", action: "Carbofuran granules at whorl" },
            { name: "Sugarcane Aphid", type: "Pest", threshold: "Colonies present", action: "Endosulfan or systemic insecticide" },
            { name: "Smut (Ustilago)", type: "Disease", threshold: "Any whips observed", action: "Remove & burn; use resistant variety" },
            { name: "Ratoon Stunting", type: "Disease", threshold: "Stunted ratoons", action: "Hot water treatment 50°C/2 hrs" },
          ].map(p => (
            <div key={p.name} style={{ padding: "9px 0", borderBottom: `1px solid ${theme.border}` }}>
              <div style={{ display: "flex", justifyContent: "space-between" }}>
                <span style={{ fontWeight: 600, fontSize: "0.83rem" }}>{p.name}</span>
                <span className={`badge ${p.type === "Pest" ? "badge-red" : "badge-gold"}`} style={{ fontSize: "0.65rem" }}>{p.type}</span>
              </div>
              <div style={{ fontSize: "0.72rem", color: theme.muted, marginTop: 2 }}>Threshold: {p.threshold}</div>
              <div style={{ fontSize: "0.72rem", color: theme.text, marginTop: 1 }}>→ {p.action}</div>
            </div>
          ))}
        </div>
      </div>
      <div className="card">
        <div className="section-header">
          <div className="card-title">Maintenance Tasks</div>
          <button className="btn btn-primary" onClick={() => openModal("addTask")}>＋ Add Task</button>
        </div>
        <div className="table-wrap">
          <table>
            <thead><tr><th>Type</th><th>Field</th><th>Date</th><th>Assignee</th><th>Notes</th><th>Status</th><th></th></tr></thead>
            <tbody>
              {maintTasks.map(t => {
                const field = fields.find(f => f.id === t.fieldId);
                return (
                  <tr key={t.id} style={{ opacity: t.status === "done" ? 0.5 : 1 }}>
                    <td className="bold">{t.type}</td>
                    <td>{field?.name || "—"}</td>
                    <td className="font-mono" style={{ fontSize: "0.78rem" }}>{t.date}</td>
                    <td>{t.assignee}</td>
                    <td style={{ color: theme.muted, fontSize: "0.78rem" }}>{t.notes}</td>
                    <td><span className={`badge ${t.status === "done" ? "badge-green" : "badge-gold"}`}>{t.status}</span></td>
                    <td><button className="btn btn-outline" style={{ padding: "3px 8px", fontSize: "0.72rem" }} onClick={() => toggleTask(t.id)}>{t.status === "done" ? "↩" : "✓"}</button></td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

// ─── HARVEST ─────────────────────────────────────────────────────────────────

function Harvest({ fields }) {
  const harvestFields = fields.filter(f => f.phase === "harvest");
  return (
    <>
      <div className="alert alert-danger mb16">🔴 {harvestFields.length} block(s) are ready for harvest. Coordinate with mill for cutting schedule and transport.</div>
      <div className="grid-2 mb16">
        <div className="card">
          <div className="card-title">Harvest-Ready Blocks</div>
          <div className="card-sub">Blocks awaiting cutting crew scheduling</div>
          {harvestFields.length === 0 ? <div className="text-muted text-sm">No blocks currently ready to harvest.</div> :
            harvestFields.map(f => (
              <div key={f.id} style={{ background: theme.surface, borderRadius: 8, padding: "14px", marginBottom: 10 }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                  <div style={{ fontWeight: 700 }}>{f.name}</div>
                  <span className="badge badge-red">Ready</span>
                </div>
                <div className="grid-2" style={{ gap: 8 }}>
                  {[["Area", f.area + " ha"], ["Variety", f.variety], ["Ratoon", `R${f.ratoon}`], ["Est. TCH", "~85"]].map(([l, v]) => (
                    <div key={l}><span style={{ fontSize: "0.65rem", color: theme.muted, fontFamily: "'DM Mono', monospace", textTransform: "uppercase" }}>{l}</span><br /><span style={{ fontWeight: 600, fontSize: "0.83rem" }}>{v}</span></div>
                  ))}
                </div>
                <div style={{ fontSize: "0.72rem", color: theme.muted, marginTop: 8 }}>{f.notes}</div>
              </div>
            ))
          }
        </div>
        <div className="card">
          <div className="card-title">Harvest Readiness Indicators</div>
          <div className="card-sub">Check these before scheduling the cut</div>
          {[
            { label: "Brix Reading", target: "> 18° Brix", status: "✅", note: "Refractometer check on juice" },
            { label: "Stalk Age", target: "12–18 months", status: "✅", note: "Verify from planting records" },
            { label: "Leaf Yellowing", target: "Lower 6–8 leaves yellow", status: "✅", note: "Visual assessment" },
            { label: "No Active Growth", target: "Arrows visible or slowed growth", status: "⚠️", note: "Check top visible internodes" },
            { label: "Mill Booking", target: "Confirmed delivery slot", status: "❌", note: "Contact mill scheduler" },
            { label: "Transport Ready", target: "Trucks & bins booked", status: "❌", note: "Coordinate logistics" },
          ].map(r => (
            <div key={r.label} style={{ display: "flex", gap: 10, padding: "8px 0", borderBottom: `1px solid ${theme.border}`, alignItems: "flex-start" }}>
              <span style={{ fontSize: "1rem" }}>{r.status}</span>
              <div>
                <div style={{ fontWeight: 600, fontSize: "0.83rem" }}>{r.label}</div>
                <div style={{ fontSize: "0.72rem", color: theme.accentGlow }}>{r.target}</div>
                <div style={{ fontSize: "0.7rem", color: theme.muted }}>{r.note}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="grid-3 mb16">
        {[
          { icon: "🔥", title: "Green Cane Harvesting", desc: "Preferred. No burning. Trash retained as mulch. Better soil health & water retention.", badge: "Recommended", badgeClass: "badge-green" },
          { icon: "🚒", title: "Burnt Cane Harvesting", desc: "Pre-harvest burn reduces trash. Faster manual cutting. Higher risk of soil degradation.", badge: "Traditional", badgeClass: "badge-gold" },
          { icon: "🤖", title: "Mechanical Harvesting", desc: "Chopper harvesters: high throughput, consistent. Requires hard flat terrain and wide rows.", badge: "Efficient", badgeClass: "badge-blue" },
        ].map(c => (
          <div className="card" key={c.title}>
            <div style={{ fontSize: "1.5rem", marginBottom: 6 }}>{c.icon}</div>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4 }}>
              <div style={{ fontWeight: 700 }}>{c.title}</div>
              <span className={`badge ${c.badgeClass}`} style={{ fontSize: "0.65rem" }}>{c.badge}</span>
            </div>
            <div style={{ fontSize: "0.78rem", color: theme.muted }}>{c.desc}</div>
          </div>
        ))}
      </div>
      <div className="card">
        <div className="card-title">Post-Harvest Ratoon Management</div>
        <div className="card-sub">Critical actions within 2 weeks of cutting</div>
        <div className="grid-3" style={{ gap: 10, marginTop: 4 }}>
          {[
            ["1", "Stub Cleaning", "Remove lodged stalks and debris from row"],
            ["2", "Trash Management", "Spread or mulch; do NOT burn if avoidable"],
            ["3", "Gap Filling", "Replant missing stools within 3 weeks"],
            ["4", "Basal Fertiliser", "Apply 40N:40P:60K at row/stool"],
            ["5", "Irrigation", "First irrigation within 3–5 days post-cut"],
            ["6", "Weed Control", "Pre-emergence herbicide before sprout flush"],
          ].map(([n, t, d]) => (
            <div key={n} style={{ background: theme.surface, borderRadius: 8, padding: "12px" }}>
              <div style={{ fontFamily: "'DM Mono', monospace", fontSize: "0.65rem", color: theme.accentGlow, marginBottom: 4 }}>STEP {n}</div>
              <div style={{ fontWeight: 600, fontSize: "0.83rem" }}>{t}</div>
              <div style={{ fontSize: "0.72rem", color: theme.muted, marginTop: 2 }}>{d}</div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

// ─── TASKS ───────────────────────────────────────────────────────────────────

function Tasks({ tasks, fields, toggleTask, openModal, deleteTask }) {
  const [filter, setFilter] = useState("all");
  const filtered = filter === "all" ? tasks : tasks.filter(t => t.status === filter);
  const sorted = [...filtered].sort((a, b) => a.date.localeCompare(b.date));
  return (
    <>
      <div className="section-header mb16">
        <div style={{ display: "flex", gap: 8 }}>
          {["all", "pending", "done"].map(f => (
            <button key={f} className={`btn ${filter === f ? "btn-primary" : "btn-outline"}`} style={{ fontSize: "0.78rem", padding: "6px 14px" }} onClick={() => setFilter(f)}>{f.charAt(0).toUpperCase() + f.slice(1)}</button>
          ))}
        </div>
        <button className="btn btn-primary" onClick={() => openModal("addTask")}>＋ Add Task</button>
      </div>
      <div className="card">
        <div className="table-wrap">
          <table>
            <thead><tr><th>Type</th><th>Field</th><th>Date</th><th>Assignee</th><th>Notes</th><th>Status</th><th>Actions</th></tr></thead>
            <tbody>
              {sorted.map(t => {
                const field = fields.find(f => f.id === t.fieldId);
                return (
                  <tr key={t.id} style={{ opacity: t.status === "done" ? 0.5 : 1 }}>
                    <td className="bold">{t.type}</td>
                    <td>{field?.name || "—"}</td>
                    <td className="font-mono" style={{ fontSize: "0.78rem" }}>{t.date}</td>
                    <td>{t.assignee}</td>
                    <td style={{ color: theme.muted, fontSize: "0.78rem", maxWidth: 180 }}>{t.notes}</td>
                    <td><span className={`badge ${t.status === "done" ? "badge-green" : "badge-gold"}`}>{t.status}</span></td>
                    <td>
                      <div style={{ display: "flex", gap: 4 }}>
                        <button className="btn btn-outline" style={{ padding: "3px 8px", fontSize: "0.7rem" }} onClick={() => toggleTask(t.id)}>{t.status === "done" ? "↩" : "✓"}</button>
                        <button className="btn btn-outline" style={{ padding: "3px 8px", fontSize: "0.7rem" }} onClick={() => openModal("editTask", t.id)}>✏️</button>
                        <button className="btn btn-danger" style={{ padding: "3px 8px", fontSize: "0.7rem" }} onClick={() => { if (confirm("Delete this task?")) deleteTask(t.id); }}>🗑</button>
                      </div>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

// ─── INVENTORY ───────────────────────────────────────────────────────────────

function Inventory({ inputs, adjustStock }) {
  const categories = [...new Set(inputs.map(i => i.category))];
  return (
    <>
      {inputs.some(i => i.qty < i.minQty) && <div className="alert alert-danger mb16">⚠️ Some inputs are below minimum stock levels. Reorder immediately to avoid operational delays.</div>}
      <div className="grid-4 mb16">
        {categories.map(cat => {
          const catItems = inputs.filter(i => i.category === cat);
          const lowItems = catItems.filter(i => i.qty < i.minQty).length;
          return (
            <div className="stat-card" key={cat}>
              <div className="stat-label">{cat}</div>
              <div className="stat-value">{catItems.length}</div>
              <div className={`stat-change ${lowItems > 0 ? "down" : "up"}`}>{lowItems > 0 ? `▼ ${lowItems} low` : "✓ All stocked"}</div>
            </div>
          );
        })}
      </div>
      <div className="card">
        <div className="card-title">Input Stock Register</div>
        <div className="card-sub">Current inventory levels and reorder status</div>
        <div className="table-wrap">
          <table>
            <thead><tr><th>Input</th><th>Category</th><th>Qty in Stock</th><th>Unit</th><th>Min. Level</th><th>Status</th><th>Unit Cost (UGX)</th><th>Adjust</th></tr></thead>
            <tbody>
              {inputs.map(i => {
                const pct = Math.min(100, (i.qty / (i.minQty * 2)) * 100);
                const low = i.qty < i.minQty;
                return (
                  <tr key={i.id}>
                    <td className="bold">{i.name}</td>
                    <td><span className="badge badge-blue" style={{ fontSize: "0.68rem" }}>{i.category}</span></td>
                    <td>
                      <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
                        <span style={{ fontFamily: "'DM Mono', monospace", fontWeight: 600 }}>{i.qty}</span>
                        <div className="progress-bar-bg" style={{ width: 80 }}>
                          <div className={`progress-bar-fill ${low ? "progress-red" : "progress-green"}`} style={{ width: `${pct}%` }} />
                        </div>
                      </div>
                    </td>
                    <td style={{ color: theme.muted, fontSize: "0.78rem" }}>{i.unit}</td>
                    <td style={{ fontFamily: "'DM Mono', monospace", fontSize: "0.78rem" }}>{i.minQty}</td>
                    <td><span className={`badge ${low ? "badge-red" : "badge-green"}`}>{low ? "⚠ Low" : "✓ OK"}</span></td>
                    <td style={{ fontFamily: "'DM Mono', monospace", fontSize: "0.78rem", color: theme.gold }}>{i.unitCost.toLocaleString()}</td>
                    <td>
                      <div style={{ display: "flex", gap: 4 }}>
                        <button className="btn btn-outline" style={{ padding: "3px 10px", fontSize: "0.8rem" }} onClick={() => adjustStock(i.id, -10)}>−</button>
                        <button className="btn btn-primary" style={{ padding: "3px 10px", fontSize: "0.8rem" }} onClick={() => adjustStock(i.id, 10)}>＋</button>
                      </div>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

// ─── MODALS ──────────────────────────────────────────────────────────────────

function FieldModal({ form, setForm, onSave, onClose, isEdit }) {
  const f = form;
  return (
    <div className="modal-overlay" onClick={e => e.target === e.currentTarget && onClose()}>
      <div className="modal">
        <div className="modal-title">{isEdit ? "Edit Block" : "Add New Block"}</div>
        <div className="grid-2">
          <div className="form-group"><label className="form-label">Block Name</label><input className="form-input" value={f.name || ""} onChange={e => setForm({ ...f, name: e.target.value })} placeholder="e.g. Block F – North" /></div>
          <div className="form-group"><label className="form-label">Area (ha)</label><input className="form-input" type="number" value={f.area || ""} onChange={e => setForm({ ...f, area: e.target.value })} /></div>
        </div>
        <div className="grid-2">
          <div className="form-group"><label className="form-label">Variety</label><select className="form-select" value={f.variety || ""} onChange={e => setForm({ ...f, variety: e.target.value })}>
            <option value="">Select...</option>
            {["NCo 376", "CP 72-2086", "Q208", "SP 80-3280", "RB 85-5536"].map(v => <option key={v}>{v}</option>)}
          </select></div>
          <div className="form-group"><label className="form-label">Phase</label><select className="form-select" value={f.phase || ""} onChange={e => setForm({ ...f, phase: e.target.value })}>
            <option value="">Select...</option>
            {Object.entries(phaseLabel).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
          </select></div>
        </div>
        <div className="grid-2">
          <div className="form-group"><label className="form-label">Soil Type</label><select className="form-select" value={f.soilType || ""} onChange={e => setForm({ ...f, soilType: e.target.value })}>
            <option value="">Select...</option>
            {["Loam", "Clay-Loam", "Sandy-Loam", "Clay", "Sand"].map(s => <option key={s}>{s}</option>)}
          </select></div>
          <div className="form-group"><label className="form-label">Ratoon #</label><input className="form-input" type="number" value={f.ratoon || 0} onChange={e => setForm({ ...f, ratoon: Number(e.target.value) })} /></div>
        </div>
        <div className="grid-2">
          <div className="form-group"><label className="form-label">Plant Date</label><input className="form-input" type="date" value={f.plantDate || ""} onChange={e => setForm({ ...f, plantDate: e.target.value })} /></div>
          <div className="form-group"><label className="form-label">Next Harvest</label><input className="form-input" type="date" value={f.nextHarvest || ""} onChange={e => setForm({ ...f, nextHarvest: e.target.value })} /></div>
        </div>
        <div className="form-group"><label className="form-label">Irrigated?</label><select className="form-select" value={f.irrigated ? "yes" : "no"} onChange={e => setForm({ ...f, irrigated: e.target.value === "yes" })}>
          <option value="yes">Yes – Irrigated</option><option value="no">No – Dryland</option>
        </select></div>
        <div className="form-group"><label className="form-label">Notes</label><textarea className="form-textarea" value={f.notes || ""} onChange={e => setForm({ ...f, notes: e.target.value })} /></div>
        <div className="modal-footer">
          <button className="btn btn-outline" onClick={onClose}>Cancel</button>
          <button className="btn btn-primary" onClick={onSave}>{isEdit ? "Save Changes" : "Add Block"}</button>
        </div>
      </div>
    </div>
  );
}

function TaskModal({ form, setForm, fields, onSave, onClose, isEdit }) {
  const f = form;
  return (
    <div className="modal-overlay" onClick={e => e.target === e.currentTarget && onClose()}>
      <div className="modal">
        <div className="modal-title">{isEdit ? "Edit Task" : "Add New Task"}</div>
        <div className="grid-2">
          <div className="form-group"><label className="form-label">Task Type</label><select className="form-select" value={f.type || ""} onChange={e => setForm({ ...f, type: e.target.value })}>
            <option value="">Select...</option>
            {["Fertilisation", "Irrigation", "Pest Scouting", "Weed Control", "Fungicide", "Trashing", "Subsoiling", "Liming", "Harvest", "Gap Filling", "Replanting"].map(t => <option key={t}>{t}</option>)}
          </select></div>
          <div className="form-group"><label className="form-label">Field</label><select className="form-select" value={f.fieldId || ""} onChange={e => setForm({ ...f, fieldId: Number(e.target.value) })}>
            <option value="">Select...</option>
            {fields.map(field => <option key={field.id} value={field.id}>{field.name}</option>)}
          </select></div>
        </div>
        <div className="grid-2">
          <div className="form-group"><label className="form-label">Date</label><input className="form-input" type="date" value={f.date || ""} onChange={e => setForm({ ...f, date: e.target.value })} /></div>
          <div className="form-group"><label className="form-label">Assignee</label><input className="form-input" value={f.assignee || ""} onChange={e => setForm({ ...f, assignee: e.target.value })} placeholder="Team or person" /></div>
        </div>
        <div className="form-group"><label className="form-label">Notes</label><textarea className="form-textarea" value={f.notes || ""} onChange={e => setForm({ ...f, notes: e.target.value })} /></div>
        <div className="modal-footer">
          <button className="btn btn-outline" onClick={onClose}>Cancel</button>
          <button className="btn btn-primary" onClick={onSave}>{isEdit ? "Save Changes" : "Add Task"}</button>
        </div>
      </div>
    </div>
  );
}        
                
