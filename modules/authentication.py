import streamlit as st
import geemap 

@st.cache_data
def authenticate():
    geemap.ee_initialize()
