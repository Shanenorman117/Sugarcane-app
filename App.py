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

st.divider()
st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
