import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Page setup for the Samsung Galaxy screen
st.set_page_config(page_title="Estate Manager", layout="centered")
st.title("🚜 Sugarcane Field Manager")

# Establish Google Sheets Connection
conn = st.connection("gsheets", type=GSheetsConnection)

tab1, tab2 = st.tabs(["Log Task", "View History"])

with tab1:
    st.subheader("Record Field Maintenance")
    with st.form("entry_form"):
        date_done = st.date_input("Date", datetime.now())
        block = st.text_input("Block No (e.g., kym025)")
        
        # Specific tasks for your agriculture work
        task = st.selectbox("Task", [
            "Manual Weeding", 
            "Ox-Plough Weeding", 
            "Herbicide Spraying", 
            "Stubble Shaving",
            "Fertilizer Application"
        ])
        
        contractor = st.text_input("Contractor/Driver Name")
        details = st.text_area("Details (e.g. Chemical name, No. of Oxen)")
        
        submit = st.form_submit_button("Save to Google Sheets")
        
        if submit:
            # Create a data row
            new_row = pd.DataFrame([{
                "Date": str(date_done),
                "Block": block,
                "Task": task,
                "Contractor": contractor,
                "Details": details
            }])
            
            # Pull current data, add new row, and upload
            try:
                existing_data = conn.read(ttl=0)
                updated_df = pd.concat([existing_data, new_row], ignore_index=True)
                conn.update(data=updated_df)
                st.success(f"✅ Successfully logged {task} for {block}!")
            except Exception as e:
                st.error("Make sure your Google Sheet 'Share' is set to 'Anyone with the link can Edit'")

with tab2:
    st.subheader("Recent Records from your Sheet")
    try:
        # Pulls the data you just saved
        data = conn.read(ttl="1m")
        st.dataframe(data.tail(10), use_container_width=True)
    except:
        st.info("No data found yet. Log your first task in the other tab!")
