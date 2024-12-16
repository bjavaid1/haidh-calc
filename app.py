import streamlit as st
import streamlit.components.v1 as components

# Title and Description
st.title("Interactive Calendar Web App")
st.write("Select days on the calendar to highlight them.")

# FullCalendar Integration
html_code = """
<!DOCTYPE html>
<html>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/main.min.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/main.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@fullcalendar/interaction@6.1.8/main.min.js"></script>
    <style>
      #calendar {
        max-width: 900px;
        margin: 0 auto;
        padding: 10px;
      }
    </style>
  </head>
  <body>
    <div id="calendar"></div>
    <script>
      document.addEventListener("DOMContentLoaded", function () {
        var calendarEl = document.getElementById("calendar");

        // Initialize the calendar
        var calendar = new FullCalendar.Calendar(calendarEl, {
          initialView: "dayGridMonth",
          selectable: true,
          headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay",
          },
          select: function (info) {
            // Send selected dates back to Streamlit
            const selectedData = JSON.stringify({
              start: info.startStr,
              end: info.endStr,
            });
            const streamlitParent = window.parent;
            streamlitParent.postMessage(selectedData, "*");
          },
        });

        calendar.render();
      });
    </script>
  </body>
</html>
"""

components.html(html_code, height=600)

st.write("### Instructions:")
st.write(
    "Use the calendar above to select days. The app will eventually calculate based on your selections."
)
