import streamlit as st
from st_iframe_postmessage import st_iframe_postmessage

st.title("Datetime Range Picker with Communication")

# Placeholder for storing datetime ranges
if "datetime_ranges" not in st.session_state:
    st.session_state["datetime_ranges"] = []

# Display current ranges in a table
st.write("### Selected Datetime Ranges")
if st.session_state["datetime_ranges"]:
    st.table(st.session_state["datetime_ranges"])
else:
    st.write("No ranges added yet. Click 'Add Range' to add.")

# Embed iframe with the datepicker.html file
st.write("### Add a New Datetime Range")
st_iframe_postmessage(
    src="html/datepicker.html",  # Path to your HTML file
    height=300,  # Adjust height as needed
    message=None,  # Initialize with no messages
)

# Listen for messages from the iframe
message = st_iframe_postmessage()

# Process and display the received message
if message:
    st.write(f"Message received from iframe: {message}")
    try:
        # Assuming message is in "start - end" format
        start, end = message.split(" - ")
        st.session_state["datetime_ranges"].append({"Start Datetime": start, "End Datetime": end})
        st.success("Datetime range added successfully!")
    except ValueError:
        st.error("Invalid datetime range format. Please check your input.")
