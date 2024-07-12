import streamlit as st

def initializeLanguage():
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    else:
        st.session_state.language = st.session_state.language