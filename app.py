import streamlit as st
import streamlit.components.v1 as components

# Title
st.title("Enhanced Interactive Calendar")

# Updated FullCalendar Integration
html_code = """
<!DOCTYPE html>
<html>
  <head>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/6.1.15/index.global.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/6.1.15/index.global.min.js"></script>
    <style>
      #calendar {
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 5px;
      }
      #reset-button {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }
      #reset-button:hover {
        background-color: #0056b3;
      }
    </style>
  </head>
  <body>
    <div id="calendar"></div>
    <button id="reset-button" onclick="resetCalendar()">Reset Calendar</button>

    <script>
      document.addEventListener("DOMContentLoaded", function () {
        var calendarEl = document.getElementById("calendar");

        var selectedDates = []; // Array to store selected date ranges

        function isDateInRange(date, start, end) {
          const d = new Date(date);
          return d >= new Date(start) && d < new Date(end);
        }

        function toggleSelection(start, end) {
          const existing = selectedDates.findIndex(event => 
            isDateInRange(event.start, start, end) && isDateInRange(start, event.start, event.end)
          );
          if (existing > -1) {
            // Remove existing selection
            selectedDates.splice(existing, 1);
          } else {
            // Add new selection
            selectedDates.push({
              title: "Selected",
              start: start,
              end: end,
              allDay: true,
              color: "#ff0000"
            });
          }
        }

        // Initialize the calendar
        var calendar = new FullCalendar.Calendar(calendarEl, {
          initialView: "dayGridMonth",
          selectable: true,
          selectOverlap: false,
          events: selectedDates, // Display selected dates as events
          select: function (info) {
            toggleSelection(info.startStr, info.endStr);
            calendar.removeAllEvents();
            calendar.addEventSource(selectedDates);
          },
        });

        // Reset the calendar
        window.resetCalendar = function () {
          selectedDates = [];
          calendar.removeAllEvents();
        };

        calendar.render();
      });
    </script>
  </body>
</html>
"""

# Embed the calendar in Streamlit app
components.html(html_code, height=700)
