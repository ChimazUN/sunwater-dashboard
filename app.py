# WEBSITE APPLICATION
# Already with data

# Import packages
import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

def main():
    st.set_page_config(
        page_title="Use Pygwalker In Streamlit",
        layout="wide"
    )
    
    st.title("Use Pygwalker In Streamlit")
    
    df = pd.read_excel('foodsales.xlsx', sheet_name="FoodSales")
    renderer = StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")
    renderer.explorer()

if __name__ == '__main__':
    main()
