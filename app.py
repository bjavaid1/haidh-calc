import streamlit as st
import streamlit.components.v1 as components

# Title
st.title("Advanced Interactive Calendar")

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
    </style>
  </head>
  <body>
    <div id="calendar"></div>
    <script>
      document.addEventListener("DOMContentLoaded", function () {
        var calendarEl = document.getElementById("calendar");

        var selectedDates = []; // Array to track selected dates

        function isSelected(date) {
          // Check if a date is in the selectedDates array
          return selectedDates.some(d => d.start === date.start && d.end === date.end);
        }

        function toggleSelection(date) {
          // Add or remove a date from the selectedDates array
          const index = selectedDates.findIndex(d => d.start === date.start && d.end === date.end);
          if (index > -1) {
            selectedDates.splice(index, 1); // Unselect
          } else {
            selectedDates.push(date); // Select
          }
        }

        // Initialize the calendar
        var calendar = new FullCalendar.Calendar(calendarEl, {
          initialView: "dayGridMonth",
          selectable: true,
          selectOverlap: false,
          events: selectedDates, // Display selected dates as events
          select: function (info) {
            const newEvent = {
              title: "Selected",
              start: info.startStr,
              end: info.endStr,
              allDay: true,
              color: "#ff0000"
            };
            toggleSelection(newEvent);
            calendar.removeAllEvents();
            calendar.addEventSource(selectedDates);
          },
        });

        // Function to reset the calendar
        window.resetCalendar = function () {
          selectedDates = [];
          calendar.removeAllEvents();
        };

        calendar.render();
      });
    </script>

    <button onclick="resetCalendar()">Reset Calendar</button>
  </body>
</html>
"""

# Embed the calendar in Streamlit app
components.html(html_code, height=700)
