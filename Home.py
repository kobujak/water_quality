import streamlit as st
import ee
from modules.nav import Navbar

st.set_page_config(layout="wide") # Page config

Navbar() # Sidebar pages
ee.Initialize()

st.title('Water quality')
st.write("There will be text")
