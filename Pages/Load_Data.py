import streamlit as st          #pip install streamlit
import csv

#Page used to display data from a previous trial

# Display title 
st.header("Load Data", divider=True)

# Display sidebar title
st.sidebar.markdown("Load Data")


file = st.file_uploader("Pick a file", type = "csv")
