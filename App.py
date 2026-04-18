import streamlit as st
import pandas as pd
from datetime import date, datetime

# \u2500\u2500\u2500 PAGE CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

st.set_page_config(
    page_title="\ud83c\udf3e CaneEstate Manager",
    page_icon="\ud83c\udf3e",
    layout="wide",
    initial_sidebar_state="expanded",
)

# \u2500\u2500\u2500 CUSTOM CSS \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Karla:wght@400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Karla', sans-serif; }

.main { background-color: #0a0f07; }
[data-testid="stSidebar"] { background-color: #111a0c; border-right: 1px solid #2a3d1e; }
[data-testid="stSidebar"] * { color: #e8f0e0 !important; }

h1, h2, h3 { font-family: 'DM Serif Display', serif !important; color: #e8f0e0; }

.metric-card {
    background: #162012; border: 1px solid #2a3d1e;
    border-radius: 10px; padding: 16px 20px; margin-bottom: 8px;
}
.metric-label { font-size: 0.72rem; color: #7a9068; text-transform: uppercase; letter-spacing: 0.06em; }
.metric-value { font-family: 'DM Serif Display', serif; font-size: 2rem; color: #e8f0e0; margin: 4px 0 2px; }
.metric-sub { font-size: 0.75rem; }

.pill {
    display: inline-block; padding: 3px 10px; border-radius: 20px;
    font-size: 0.72rem; font-weight: 600;
}
.pill-prep  { background: rgba(201,168,76,0.15); color: #c9a84c; }
.pill-plant { background: rgba(93,176,58,0.15);  color: #7ed957; }
.pill-maintain { background: rgba(74,176,224,0.15); color: #4ab0e0; }
.pill-harvest { background: rgba(224,92,74,0.15); color: #e05c4a; }
.pill-fallow  { background: rgba(122,144,104,0.15); color: #7a9068; }

.alert-box {
    border-radius: 8px; padding: 10px 14px;
    font-size: 0.85rem; margin-bottom: 10px;
}
.alert-warn    { background: rgba(224,168,74,0.1);  border: 1px solid rgba(224,168,74,0.3);  color: #e0a84a; }
.alert-danger  { background: rgba(224,92,74,0.1);   border: 1px solid rgba(224,92,74,0.3);   color: #e05c4a; }
.alert-success { background: rgba(93,176,58,0.1);   border: 1px solid rgba(93,176,58,0.3);   color: #7ed957; }
.alert-info    { background: rgba(74,176,224,0.1);  border: 1px solid rgba(74,176,224,0.3);  color: #4ab0e0; }

.section-card {
    background: #162012; border: 1px solid #2a3d1e;
    border-radius: 10px; padding: 20px; margin-bottom: 16px;
}
.tl-done  { color: #7ed957; }
.tl-cur   { color: #e0a84a; }
.tl-pend  { color: #7a9068; }

div[data-testid="stDataFrame"] { background: #162012; }
</style>
""", unsafe_allow_html=True)

# \u2500\u2500\u2500 SESSION STATE INIT \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

def init_state():
    if "fields" not in st.session_state:
        st.session_state.fields = [
            {"id": 1, "name": "Block A \u2013 North",   "area": 45, "variety": "NCo 376",    "phase": "maintain", "plantDate": "2024-03-10", "nextHarvest": "2025-09-10", "ratoon": 2, "soilType": "Loam",       "irrigated": True,  "notes": "Good stand, monitor for borer"},
            {"id": 2, "name": "Block B \u2013 South",   "area": 30, "variety": "CP 72-2086", "phase": "harvest",  "plantDate": "2023-11-05", "nextHarvest": "2025-05-05", "ratoon": 3, "soilType": "Clay-Loam",  "irrigated": True,  "notes": "Ready for harvest \u2014 TCH ~85t"},
            {"id": 3, "name": "Block C \u2013 East",    "area": 20, "variety": "NCo 376",    "phase": "prep",     "plantDate": "",           "nextHarvest": "",           "ratoon": 0, "soilType": "Sandy-Loam", "irrigated": False, "notes": "Sub-soiling in progress"},
            {"id": 4, "name": "Block D \u2013 West",    "area": 38, "variety": "Q208",       "phase": "plant",    "plantDate": "2025-02-15", "nextHarvest": "2026-08-15", "ratoon": 1, "soilType": "Loam",       "irrigated": True,  "notes": "Newly planted plant crop"},
            {"id": 5, "name": "Block E \u2013 Central", "area": 25, "variety": "CP 72-2086", "phase": "fallow",   "plantDate": "",           "nextHarvest": "",           "ratoon": 0, "soilType": "Clay",       "irrigated": False, "notes": "Fallow \u2013 green manure crop sown"},
        ]
    if "tasks" not in st.session_state:
        st.session_state.tasks = [
            {"id": 1, "fieldId": 1, "type": "Fertilisation",  "date": "2025-04-25", "status": "pending", "notes": "Top dressing \u2014 200 kg/ha Urea",    "assignee": "Team A"},
            {"id": 2, "fieldId": 2, "type": "Harvest",        "date": "2025-05-01", "status": "pending", "notes": "Mechanical harvest \u2014 Block B",      "assignee": "Harvest Crew"},
            {"id": 3, "fieldId": 3, "type": "Subsoiling",     "date": "2025-04-20", "status": "done",    "notes": "Deep rip to 60cm complete",         "assignee": "Team B"},
            {"id": 4, "fieldId": 4, "type": "Irrigation",     "date": "2025-04-18", "status": "done",    "notes": "Drip irrigation cycle 3",           "assignee": "Irrigation"},
            {"id": 5, "fieldId": 1, "type": "Pest Scouting",  "date": "2025-04-22", "status": "pending", "notes": "Check for stalk borer damage",      "assignee": "Scout A"},
            {"id": 6, "fieldId": 3, "type": "Liming",         "date": "2025-04-30", "status": "pending", "notes": "Apply 2t/ha dolomitic lime",        "assignee": "Team B"},
            {"id": 7, "fieldId": 5, "type": "Ox Weeding",     "date": "2025-04-19", "status": "done",    "notes": "1st ox cultivation pass complete",  "assignee": "Team C"},
        ]
    if "inputs" not in st.session_state:
        st.session_state.inputs = [
            {"id": 1, "name": "Urea (46% N)",          "category": "Fertiliser",  "unit": "bags (50kg)", "qty": 420, "minQty": 100, "unitCost": 92000},
            {"id": 2, "name": "DAP (18-46-0)",          "category": "Fertiliser",  "unit": "bags (50kg)", "qty": 180, "minQty": 50,  "unitCost": 115000},
            {"id": 3, "name": "KCl Muriate of Potash",  "category": "Fertiliser",  "unit": "bags (50kg)", "qty": 95,  "minQty": 50,  "unitCost": 105000},
            {"id": 4, "name": "Atrazine 500SC",         "category": "Herbicide",   "unit": "litres",      "qty": 38,  "minQty": 20,  "unitCost": 45000},
            {"id": 5, "name": "Carbofuran 5G",          "category": "Pesticide",   "unit": "kg",          "qty": 12,  "minQty": 20,  "unitCost": 28000},
            {"id": 6, "name": "Glyphosate 480SL",       "category": "Herbicide",   "unit": "litres",      "qty": 55,  "minQty": 25,  "unitCost": 32000},
            {"id": 7, "name": "NCo 376 Seed Cane",      "category": "Seed Cane",   "unit": "tonnes",      "qty": 4,   "minQty": 10,  "unitCost": 380000},
        ]
    if "next_id" not in st.session_state:
        st.session_state.next_id = 100

init_state()

# \u2500\u2500\u2500 HELPERS \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

PHASE_LABELS = {"prep": "Land Prep", "plant": "Planting", "maintain": "Maintenance", "harvest": "Harvest", "fallow": "Fallow"}
PHASE_EMOJI  = {"prep": "\ud83d\udfe1", "plant": "\ud83d\udfe2", "maintain": "\ud83d\udd35", "harvest": "\ud83d\udd34", "fallow": "\u26ab"}
VARIETIES    = ["NCo 376", "CP 72-2086", "Q208", "SP 80-3280", "RB 85-5536"]
SOIL_TYPES   = ["Loam", "Clay-Loam", "Sandy-Loam", "Clay", "Sand"]
TASK_TYPES   = ["Fertilisation", "Irrigation", "Pest Scouting", "Weed Control", "Ox Weeding",
                "Manual Weeding", "Fungicide", "Trashing", "Subsoiling", "Liming",
                "Harvest", "Gap Filling", "Replanting"]

def field_name(fid):
    for f in st.session_state.fields:
        if f["id"] == fid:
            return f["name"]
    return "\u2014"

def next_id():
    st.session_state.next_id += 1
    return st.session_state.next_id

def total_area():
    return sum(f["area"] for f in st.session_state.fields)

def pending_count():
    return sum(1 for t in st.session_state.tasks if t["status"] == "pending")

def low_stock_count():
    return sum(1 for i in st.session_state.inputs if i["qty"] < i["minQty"])

def harvest_ready():
    return [f for f in st.session_state.fields if f["phase"] == "harvest"]

# \u2500\u2500\u2500 SIDEBAR \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

with st.sidebar:
    st.markdown("## \ud83c\udf3e CaneEstate")
    st.caption("Sugar Cane Estate Manager v1.0")
    st.markdown("---")
    st.caption(f"\ud83d\udcc5 Season: **2024 / 2025**   \ud83d\udfe2 Active")
    st.markdown("---")

    page = st.radio(
        "Navigation",
        options=[
            "\ud83c\udf3f  Overview",
            "\ud83d\uddfa\ufe0f  Field Registry",
            "\ud83d\ude9c  Land Preparation",
            "\ud83c\udf31  Planting",
            "\ud83d\udd27  Maintenance",
            "\u2699\ufe0f  Harvest",
            "\ud83d\udccb  Task Schedule",
            "\ud83d\udce6  Input Inventory",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")
    pc = pending_count()
    ls = low_stock_count()
    if pc:
        st.warning(f"\ud83d\udccb **{pc}** pending tasks")
    if ls:
        st.error(f"\ud83d\udce6 **{ls}** inputs low on stock")

# \u2500\u2500\u2500 OVERVIEW \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

if page == "\ud83c\udf3f  Overview":
    st.title("\ud83c\udf3e Estate Overview")
    st.caption(f"Season 2024/2025  \u00b7  {date.today().strftime('%A, %d %B %Y')}")

    hr = harvest_ready()
    if hr:
        st.error(f"\ud83d\udd34 **{len(hr)} block(s) ready for harvest.** Coordinate with mill and transport.")
    if low_stock_count():
        st.warning(f"\u26a0\ufe0f **{low_stock_count()} input(s)** are below minimum stock levels.")
    st.success("\u2705 Subsoiling on Block C completed. Primary tillage scheduled for 2025-04-25.")

    # KPI metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Area (ha)", total_area())
    col2.metric("Est. Yield (TCH)", "~82 t/ha", "+4 vs last season")
    col3.metric("Pending Tasks", pending_count())
    col4.metric("Low Stock Items", low_stock_count())

    st.markdown("---")
    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Field Phase Breakdown")
        phase_counts = {p: 0 for p in PHASE_LABELS}
        for f in st.session_state.fields:
            phase_counts[f["phase"]] = phase_counts.get(f["phase"], 0) + 1
        for ph, cnt in phase_counts.items():
            emoji = PHASE_EMOJI[ph]
            label = PHASE_LABELS[ph]
            pct = int((cnt / max(len(st.session_state.fields), 1)) * 100)
            st.markdown(f"**{emoji} {label}** \u2014 {cnt} block(s)")
            st.progress(pct / 100)

    with col_b:
        st.subheader("Upcoming Tasks")
        sorted_tasks = sorted(st.session_state.tasks, key=lambda t: t["date"])[:6]
        for t in sorted_tasks:
            icon = "\u2705" if t["status"] == "done" else "\u23f3"
            fn = field_name(t["fieldId"])
            st.markdown(f"{icon} **{t['type']}** \u2014 {fn}  \n`{t['date']}` \u00b7 {t['assignee']}")

    st.markdown("---")
    st.subheader("Estate Field Summary")
    rows = []
    for f in st.session_state.fields:
        rows.append({
            "Block": f["name"],
            "Area (ha)": f["area"],
            "Variety": f["variety"],
            "Phase": PHASE_EMOJI[f["phase"]] + " " + PHASE_LABELS[f["phase"]],
            "Ratoon": "Plant Crop" if f["ratoon"] == 0 else f"R{f['ratoon']}",
            "Next Harvest": f["nextHarvest"] or "\u2014",
            "Irrigated": "\u2705" if f["irrigated"] else "\u274c",
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

# \u2500\u2500\u2500 FIELD REGISTRY \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

elif page == "\ud83d\uddfa\ufe0f  Field Registry":
    st.title("\ud83d\uddfa\ufe0f Field Registry")
    st.caption(f"{len(st.session_state.fields)} blocks \u00b7 {total_area()} ha total")

    with st.expander("\u2795 Add New Block", expanded=False):
        with st.form("add_field_form"):
            c1, c2 = st.columns(2)
            fn  = c1.text_input("Block Name", placeholder="e.g. Block F \u2013 South West")
            fa  = c2.number_input("Area (ha)", min_value=0.1, step=0.5, value=10.0)
            c3, c4 = st.columns(2)
            fv  = c3.selectbox("Variety", VARIETIES)
            fph = c4.selectbox("Phase", list(PHASE_LABELS.keys()), format_func=lambda x: PHASE_LABELS[x])
            c5, c6 = st.columns(2)
            fst = c5.selectbox("Soil Type", SOIL_TYPES)
            fra = c6.number_input("Ratoon #", min_value=0, max_value=10, value=0)
            c7, c8 = st.columns(2)
            fpd = c7.date_input("Plant Date", value=None)
            fnh = c8.date_input("Next Harvest", value=None)
            fi  = st.checkbox("Irrigated?", value=True)
            fno = st.text_area("Notes", height=60)
            if st.form_submit_button("\u2705 Add Block", use_container_width=True):
                if fn:
                    st.session_state.fields.append({
                        "id": next_id(), "name": fn, "area": fa, "variety": fv,
                        "phase": fph, "plantDate": str(fpd) if fpd else "",
                        "nextHarvest": str(fnh) if fnh else "",
                        "ratoon": fra, "soilType": fst, "irrigated": fi, "notes": fno,
                    })
                    st.success(f"Block **{fn}** added.")
                    st.rerun()
                else:
                    st.error("Block name is required.")

    st.markdown("---")

    for idx, f in enumerate(st.session_state.fields):
        with st.expander(f"{PHASE_EMOJI[f['phase']]} **{f['name']}** \u2014 {f['area']} ha \u00b7 {PHASE_LABELS[f['phase']]}"):
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Variety",  f["variety"])
            col2.metric("Soil",     f["soilType"])
            col3.metric("Ratoon",   "Plant Crop" if f["ratoon"] == 0 else f"R{f['ratoon']}")
            col4.metric("Irrigated", "Yes" if f["irrigated"] else "No")

            c5, c6 = st.columns(2)
            c5.markdown(f"\ud83d\udcc5 **Planted:** {f['plantDate'] or '\u2014'}")
            c6.markdown(f"\ud83c\udf3e **Harvest ETA:** {f['nextHarvest'] or '\u2014'}")
            if f["notes"]:
                st.info(f"\ud83d\udcac {f['notes']}")

            pending = [t for t in st.session_state.tasks if t["fieldId"] == f["id"] and t["status"] == "pending"]
            if pending:
                st.warning(f"\ud83d\udccb {len(pending)} pending task(s) on this block.")

            with st.form(f"edit_field_{f['id']}"):
                st.markdown("**Edit Block**")
                ec1, ec2 = st.columns(2)
                en  = ec1.text_input("Name",  value=f["name"],    key=f"en_{f['id']}")
                ea  = ec2.number_input("Area (ha)", value=float(f["area"]), min_value=0.1, step=0.5, key=f"ea_{f['id']}")
                ec3, ec4 = st.columns(2)
                ev  = ec3.selectbox("Variety",  VARIETIES, index=VARIETIES.index(f["variety"]) if f["variety"] in VARIETIES else 0, key=f"ev_{f['id']}")
                eph = ec4.selectbox("Phase", list(PHASE_LABELS.keys()), index=list(PHASE_LABELS.keys()).index(f["phase"]), format_func=lambda x: PHASE_LABELS[x], key=f"eph_{f['id']}")
                ec5, ec6 = st.columns(2)
                est = ec5.selectbox("Soil", SOIL_TYPES, index=SOIL_TYPES.index(f["soilType"]) if f["soilType"] in SOIL_TYPES else 0, key=f"est_{f['id']}")
                era = ec6.number_input("Ratoon #", value=f["ratoon"], min_value=0, max_value=10, key=f"era_{f['id']}")
                eir = st.checkbox("Irrigated?", value=f["irrigated"], key=f"eir_{f['id']}")
                eno = st.text_area("Notes", value=f["notes"], height=60, key=f"eno_{f['id']}")
                s1, s2 = st.columns(2)
                if s1.form_submit_button("\ud83d\udcbe Save Changes", use_container_width=True):
                    st.session_state.fields[idx].update({
                        "name": en, "area": ea, "variety": ev, "phase": eph,
                        "soilType": est, "ratoon": era, "irrigated": eir, "notes": eno,
                    })
                    st.success("Saved.")
                    st.rerun()
                if s2.form_submit_button("\ud83d\uddd1\ufe0f Delete Block", use_container_width=True):
                    st.session_state.fields.pop(idx)
                    st.warning("Block deleted.")
                    st.rerun()

# \u2500\u2500\u2500 LAND PREPARATION \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

elif page == "\ud83d\ude9c  Land Preparation":
    st.title("\ud83d\ude9c Land Preparation")
    st.info("\ud83d\udcd8 Land preparation is the foundation of a productive sugarcane crop. Proper tillage, drainage and soil conditioning significantly impact stand establishment and long-term yields.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Preparation Stages")
        stages = [
            ("Site Assessment & Soil Analysis", "Soil sampling, pH test, drainage evaluation", "done"),
            ("Land Clearing", "Remove crop residues, stumps, trees", "done"),
            ("Deep Sub-soiling / Ripping", "Break hardpan at 50\u201370 cm depth", "done"),
            ("Primary Tillage (Ploughing)", "Mouldboard / ox plough 30\u201340 cm", "current"),
            ("Liming & Soil Amendments", "Adjust pH, apply gypsum if needed", "pending"),
            ("Secondary Tillage (Harrowing)", "Break clods, level surface", "pending"),
            ("Drainage & Road Construction", "Grade drains, internal roads", "pending"),
            ("Furrow Making / Row Marking", "Mark rows at 1.5\u20131.8 m spacing", "pending"),
        ]
        for i, (label, desc, status) in enumerate(stages):
            icon = "\u2705" if status == "done" else ("\ud83d\udd04" if status == "current" else "\u2b55")
            st.markdown(f"**{icon} {i+1}. {label}**  \n_{desc}_")

        st.markdown("---")
        st.subheader("Soil Requirements")
        req = pd.DataFrame([
            ["Soil pH",        "5.5 \u2013 6.5",        "Adjust with lime or sulphur"],
            ["Organic Matter", "> 2.5%",            "Incorporate trash / green manure"],
            ["Drainage",       "< 50 cm water table","Install drains if needed"],
            ["Tillage Depth",  "40 \u2013 60 cm",        "Break compaction layers"],
            ["Row Spacing",    "1.5 \u2013 1.8 m",       "Standard for ox / mechanised ops"],
            ["Slope",          "< 8%",              "Terrace on steeper slopes"],
        ], columns=["Parameter", "Target", "Note"])
        st.dataframe(req, use_container_width=True, hide_index=True)

    with col2:
        st.subheader("Equipment Checklist")
        equip = [
            ("\ud83d\ude9c", "Sub-soiler / Ripper",    "Heavy-duty 3\u20135 tine, 50\u201370 cm depth"),
            ("\ud83d\udd04", "Mouldboard Plough",      "Primary tillage, 30\u201340 cm"),
            ("\ud83d\udc02", "Ox Plough",              "Animal-drawn mouldboard; ideal for smallholder & mid-scale plots"),
            ("\u2699\ufe0f", "Disc Harrow",            "Secondary tillage, clod breaking"),
            ("\ud83d\udccf", "Ridger / Furrower",      "Forming planting furrows"),
            ("\ud83d\udc02", "Ox Ridger",              "Animal-drawn ridger for inter-row furrow opening"),
            ("\ud83c\udf0a", "Grader / Excavator",     "Drain construction"),
            ("\ud83c\udf3f", "Spray Rig",              "Pre-plant herbicide application"),
        ]
        for icon
