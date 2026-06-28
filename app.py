import streamlit as st

# Read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display HTML in Streamlit
st.components.v1.html(html_code, height=600, scrolling=True)
