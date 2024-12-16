import streamlit as st
import streamlit.components.v1 as components

# Title
st.title("HTML Integration Test")

# Simple HTML Block
html_code = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        text-align: center;
        padding: 20px;
      }
      .box {
        padding: 20px;
        background-color: lightblue;
        border: 2px solid blue;
        border-radius: 10px;
        display: inline-block;
      }
    </style>
  </head>
  <body>
    <div class="box">
      <h2>Hello, Streamlit!</h2>
      <p>This is a simple HTML block to test embedding capabilities.</p>
    </div>
  </body>
</html>
"""

# Embed HTML
components.html(html_code, height=300)
