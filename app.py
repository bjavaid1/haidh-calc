import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

st.title("Datetime Range Entry with Logging")

# Placeholder for storing datetime ranges
if "datetime_ranges" not in st.session_state:
    st.session_state["datetime_ranges"] = []

# Display current ranges in a table
st.write("### Selected Datetime Ranges")
if st.session_state["datetime_ranges"]:
    df = pd.DataFrame(st.session_state["datetime_ranges"], columns=["Start Datetime", "End Datetime"])
    st.table(df)
else:
    st.write("No ranges added yet. Click 'Add Range' to add.")

# Add Range button to trigger manual datetime entry form
if st.button("Add Range"):
    logger.debug("Add Range button clicked. Displaying form...")
    components.html(
        open("html/datepicker.html").read(),
        height=300,
    )

# Function to add a new range to the table
def add_new_range(range_value):
    logger.debug(f"Received range from HTML: {range_value}")
    try:
        start, end = range_value.split(" - ")
        st.session_state["datetime_ranges"].append({"Start Datetime": start, "End Datetime": end})
        logger.info(f"Added range: {start} - {end}")
    except ValueError:
        st.error("Invalid format. Please enter both start and end datetimes.")
        logger.error("Invalid datetime range format received.")

# JavaScript listener to capture messages from the HTML
components.html(
    """
    <script>
        const streamlitParent = window.parent;
        window.addEventListener("message", (event) => {
            if (event.data) {
                console.log("Message received from HTML:", event.data); // Debug log in browser console
                streamlitParent.postMessage(event.data, "*");
            }
        });
    </script>
    """,
    height=0,
)

# Process received messages
if "last_range" not in st.session_state:
    st.session_state["last_range"] = None

# Capture messages sent to Streamlit
message = st.experimental_get_query_params().get("message", None)

if message and message[0]:
    logger.debug(f"Message received in Streamlit: {message[0]}")
    add_new_range(message[0])
