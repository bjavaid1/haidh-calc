import streamlit as st
import pandas as pd

st.title("Datetime Range Picker")

# Placeholder for storing datetime ranges
if "datetime_ranges" not in st.session_state:
    st.session_state["datetime_ranges"] = []

# Display current ranges in a table
st.write("### Selected Datetime Ranges")
if st.session_state["datetime_ranges"]:
    df = pd.DataFrame(st.session_state["datetime_ranges"], columns=["Start Datetime", "End Datetime"])
    st.table(df)
else:
    st.write("No ranges added yet. Use the form below to add a range.")

# Form to add a new datetime range
with st.form("datetime_form", clear_on_submit=True):
    st.write("### Add a New Datetime Range")
    start_datetime = st.text_input("Start Datetime (e.g., 2024-12-15 14:30)")
    end_datetime = st.text_input("End Datetime (e.g., 2024-12-15 16:00)")
    submitted = st.form_submit_button("Add Range")

    if submitted:
        try:
            # Validate input format (basic check)
            if not start_datetime or not end_datetime:
                st.error("Both start and end datetime fields are required.")
            else:
                # Add the datetime range to the session state
                st.session_state["datetime_ranges"].append([start_datetime, end_datetime])
                st.success("Datetime range added successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
