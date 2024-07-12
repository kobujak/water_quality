import streamlit as st
from modules.nav import Navbar
from modules.language import initializeLanguage
import gettext
_ = gettext.gettext

st.set_page_config(layout="wide") # Page config
initializeLanguage()

Navbar() # Sidebar pages


try:
  localizator = gettext.translation('Home', localedir='locales', languages=[st.session_state.language])
  localizator.install()
  _ = localizator.gettext 
except:
    pass
st.title(_('Home_title'),anchor=False)
col1, col2, col3 = st.columns(3,gap="large")
with col1:
  st.markdown('#')
with col2:
  st.markdown('#')
  st.subheader(_('Home_Description'),anchor=False)
with col3:
  st.markdown('#')



