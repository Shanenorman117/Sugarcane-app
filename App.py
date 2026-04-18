import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Set up the page
st.set_page_config(page_title="Sugarcane Field Logs", layout="wide")

# Establish Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🚜 Sugarcane Estate Field Logger")
st.write("Enter daily field operations and labor details below.")

# Create the input form
with st.form("entry_form", clear_on_submit=True):
    st.subheader("General Information")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        date = st.date_input("Date")
    with col_b:
        block = st.text_input("Block Name/Number")
    with col_c:
        area = st.number_input("Area Worked (Ha)", min_value=0.0, step=0.1)

    st.divider()

    # Land Preparation Section
    st.subheader("Land Preparation & Planting")
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        first_plough = st.number_input("1st Plough Area", min_value=0.0)
        second_plough = st.number_input("2nd Plough Area", min_value=0.0)
    with col_p2:
        third_plough = st.number_input("3rd Plough Area", min_value=0.0)
        fourth_plough = st.number_input("4th Plough Area", min_value=0.0)
    with col_p3:
        ridged = st.number_input("Ridged Area", min_value=0.0)
        planted = st.number_input("Planted Area", min_value=0.0)

    st.divider()

    # Weeding & Slashing Section
    st.subheader("Weeding & Slashing")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        full_weeding = st.number_input("Full Weeding (Man-days/Area)", min_value=0.0)
        spot_weeding = st.number_input("Spot Weeding (Man-days/Area)", min_value=0.0)
    with col_w2:
        heavy_slashing = st.number_input("Heavy Slashing", min_value=0.0)
        light_slashing = st.number_input("Light Slashing", min_value=0.0)

    st.divider()

    # Extras Section
    st.subheader("Additional Details")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        ox_plough = st.number_input("Ox Plough Area", min_value=0.0)
        herbicides = st.text_input("Herbicides Used")
    with col_e2:
        contractor = st.text_input("Contractor")
        remarks = st.text_area("Remarks")

    # Submit Button
    submit_button = st.form_submit_button("Save to Google Sheets")

    if submit_button:
        if block == "":
            st.error("Please enter a Block name.")
        else:
            # Create a dataframe with the new entry
            # Ensure these keys match your Google Sheet column headers exactly
            new_row = pd.DataFrame([{
                "date": str(date),
                "block": block,
                "area": area,
                "1st plough": first_plough,
                "2nd plough": second_plough,
                "3rd plough": third_plough,
                "4th plough": fourth_plough,
                "ridged": ridged,
                "planted": planted,
                "full weeding": full_weeding,
                "spot weeding": spot_weeding,
                "heavy slashing": heavy_slashing,
                "light slashing": light_slashing,
                "ox plough": ox_plough,
                "herbicides": herbicides,
                "contractor": contractor,
                "remarks": remarks
            }])

            try:
                # Fetch existing data
                existing_data = conn.read(worksheet="Sheet1") # Change Sheet1 to your tab name if different
                
                # Add the new row
                updated_df = pd.concat([existing_data, new_row], ignore_index=True)
                
                # Update the Google Sheet
                conn.update(worksheet="Sheet1", data=updated_df)
                
                st.success(f"Successfully recorded data for {block}!")
            except Exception as e:
                st.error(f"Error: {e}")
