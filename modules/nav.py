import streamlit as st


def Navbar():
    with st.sidebar:
        st.page_link('Home.py', label='Home', icon='🏠')
        st.page_link('pages/NDWI.py', label='NDWI', icon='🔎')
        st.page_link('pages/NDTI.py', label='NDTI', icon='🔎')
        st.page_link('pages/NDSI.py', label='NDSI', icon='🔎')
        st.page_link('pages/CDOM.py', label='CDOM', icon='🦠')
        st.page_link('pages/CHLA.py', label='CHLA', icon='🦠')
        st.page_link('pages/CYA.py', label='CYA', icon='🦠')
        st.page_link('pages/DOC.py', label='DOC', icon='🦠')
        st.page_link('pages/Turbidity.py', label='Turbidity', icon='💧')
        st.page_link('pages/Lakes_Analysis.py', label='Lakes Analysis', icon='📈')