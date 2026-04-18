import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Page setup
st.set_page_config(page_title="Sugarcane Estate Manager", layout="centered")

# Establish Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🚜 Sugarcane Estate Operations")

with st.form("main_form", clear_on_submit=True):
    # Section 1: Core Info
    st.subheader("📍 Field Details")
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Date")
        block = st.text_input("Block Number/Name")
    with col2:
        contractor = st.text_input("Contractor/Supervisor")
        
    st.divider()

    # Section 2: Land Preparation (Specific Stages)
    st.subheader("🏗️ Land Preparation Section")
    lp_col1, lp_col2 = st.columns(2)
    with lp_col1:
        p1 = st.number_input("1st Plough (Ha)", min_value=0.0)
        p2 = st.number_input("2nd Plough (Ha)", min_value=0.0)
        p3 = st.number_input("3rd Plough (Ha)", min_value=0.0)
    with lp_col2:
        p4 = st.number_input("4th Plough (Ha)", min_value=0.0)
        ridge = st.number_input("Ridging (Ha)", min_value=0.0)
        plant = st.number_input("Planting (Ha)", min_value=0.0)

    st.divider()

    # Section 3: Maintenance & Other Activities
    st.subheader("🌿 General Activities & Weeding")
    activity = st.selectbox("Select Maintenance Activity", [
        "None", "Full Weeding", "Spot Weeding", 
        "Heavy Slashing", "Light Slashing", "Ox Plough", "Herbicide Application"
    ])
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        act_area = st.number_input("Activity Area (Ha)", min_value=0.0)
    with m_col2:
        price_ha = st.number_input("Price per Ha (UGX)", min_value=0)

    total_act_cost = act_area * price_ha
    if activity != "None":
        st.info(f"Activity Cost: {total_act_cost:,} UGX")

    st.divider()
    remarks = st.text_area("Additional Remarks")
    
    submit = st.form_submit_button("Submit Record to Sheets")

    if submit:
        if not block:
            st.error("Please provide the Block name.")
        else:
            # Prepare row for Google Sheets
            new_entry = pd.DataFrame([{
                "Date": str(date),
                "Block": block,
                "Contractor": contractor,
                "1st Plough": p1,
                "2nd Plough": p2,
                "3rd Plough": p3,
                "4th Plough": p4,
                "Ridging": ridge,
                "Planting": plant,
                "Other Activity": activity,
                "Activity Area": act_area,
                "Price per Ha": price_ha,
                "Activity Cost": total_act_cost,
                "Remarks": remarks
            }])

            try:
                # Use the URL from your Secrets to find the sheet
                sheet_url = st.secrets["public_gsheets_url"]
                
                # Read existing data and append
                df = conn.read(spreadsheet=sheet_url)
                updated_df = pd.concat([df, new_entry], ignore_index=True)
                
                # Save it back to Google
                conn.update(spreadsheet=sheet_url, data=updated_df)
                
                st.success(f"Record for {block} uploaded successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
