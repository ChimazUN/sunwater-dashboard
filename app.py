# Import packages
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

# Page Settings
st.set_page_config(
    page_title="Data Dashboard",
    page_icon=":classical_building:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title & subtitle of page
st.title("Sunwater Intern Data Analytics Dashboard")
st.subheader('Upload your dataset here and create a dashboard.')

# Add a paragraph and a link
st.markdown("""
    <p>
        Welcome to the Data Dashboard. Here, you can upload your dataset and use various tools to generate insightful charts and graphs.
        For a tutorial on how to use this tool, please watch the following video: 
        <a href="https://youtu.be/3WjWeH3HIMo?t=168" target="_blank">DASHBOARD TUTORIAL</a> (you can ignore the first 2 minutes & 47 seconds)
    </p>
    """, unsafe_allow_html=True)

# Uploading Data
uploaded_file = st.file_uploader("your csv data (MUST be .csv file)")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    renderer = StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")
    renderer.explorer()



