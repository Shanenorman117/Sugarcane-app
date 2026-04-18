import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration for Mobile
st.set_page_config(page_title="Estate Supervisor Pro", layout="centered")

st.title("🚜 Estate Supervisor Dashboard")
st.subheader("Masindi & Kiryandongo Operations")

# --- TAB NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["Land Status", "Labor Log", "Machinery"])

# --- TAB 1: LAND STATUS ---
with tab1:
    st.header("Sugarcane Block Tracking")
    block_no = st.text_input("Block Number (e.g., kym025)")
    variety = st.selectbox("Variety", ["SSP", "CO945", "R858", "FR95 2345"])
    status = st.select_slider("Operation Status", 
                             options=["Ploughed", "1st Ratoon", "2nd Ratoon", "Harvested"])
    
    if st.button("Update Block Status"):
        st.success(f"Block {block_no} updated to {status} ({variety})")
        # In a real app, this would save to a database.

# --- TAB 2: LABOR & PAYROLL ---
with tab2:
    st.header("Labor Report")
    contractor = st.selectbox("Contractor", ["Mujuni", "Etyanga Daniel", "Oyet Alfred", "Byaruhanga Ernest"])
    work_type = st.selectbox("Task", ["Weeding", "Stubble Shaving", "Ploughing", "Planting"])
    rate = st.number_input("Rate per Ha (UGX)", value=50000)
    ha_done = st.number_input("Hectares Completed", step=0.1)
    
    total_pay = rate * ha_done
    st.metric("Total Payment Due", f"{total_pay:,.0f} UGX")
    
    if st.button("Log Labor Payment"):
        st.info(f"Payment logged for {contractor}")

# --- TAB 3: MACHINERY ---
with tab3:
    st.header("Fleet & Fuel")
    vehicle = st.selectbox("Vehicle", ["FAW Truck", "Sinotruk NX371", "Bajaj BM 100"])
    fuel_added = st.number_input("Fuel Added (Liters)")
    odometer = st.number_input("Current Odometer/Hours")
    
    if st.button("Save Machinery Log"):
        st.write(f"Logged {fuel_added}L for {vehicle} at {odometer} mark.")
# --- NEW SECTION: FIELD MAINTENANCE ---
with tab2:
    st.header("Field Maintenance Log")
    
    # Selection of the Block being worked on
    target_block = st.text_input("Block Number", placeholder="e.g., kym025")
    
    # Maintenance Category
    maint_type = st.selectbox("Maintenance Task", [
        "Manual Weeding", 
        "Ox-Plough Weeding", 
        "Herbicide Spraying", 
        "Fertilizer Application",
        "Stubble Shaving"
    ])
    
    col1, col2 = st.columns(2)
    with col1:
        date_done = st.date_input("Date of Task")
    with col2:
        man_power = st.number_input("Number of People/Oxen", min_value=1)

    # Specifics for Spraying
    if maint_type == "Herbicide Spraying":
        chemical = st.text_input("Chemical Name (e.g., 2,4-D, Glyphosate)")
        knapsacks = st.number_input("Number of Knapsacks used", min_value=1)
        st.caption(f"Tracking {chemical} application for {target_block}")

    # Specifics for Ox-Plough
    if maint_type == "Ox-Plough Weeding":
        ox_pairs = st.number_input("Number of Oxen Pairs", min_value=1)
        contractor = st.text_input("Ox-Plough Contractor")

    if st.button("Save Maintenance Record"):
        st.success(f"Successfully logged {maint_type} for Block {target_block}")

st.divider()
st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
