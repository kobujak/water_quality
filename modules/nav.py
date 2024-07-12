import streamlit as st
import gettext
_ = gettext.gettext


def Navbar():
    _ = gettext.gettext
    try:
        localizator = gettext.translation('nav', localedir='locales', languages=[st.session_state.language])
        localizator.install()
        _ = localizator.gettext 
    except:
        pass
    st.sidebar.selectbox(_('Select language'), ['en', 'pl'],key = 'language')
    st.sidebar.page_link('Home.py', label=_('Home'), icon='🏠')
    st.sidebar.page_link('pages/NDWI.py', label=_('NDWI'), icon='🔎')
    st.sidebar.page_link('pages/NDTI.py', label=_('NDTI'), icon='🔎')
    st.sidebar.page_link('pages/NDVI.py', label=_('NDVI'), icon='🔎')
    st.sidebar.page_link('pages/CDOM.py', label=_('CDOM'), icon='🦠')
    st.sidebar.page_link('pages/CHLA.py', label=_('CHLA'), icon='🦠')
    st.sidebar.page_link('pages/CYA.py', label=_('CYA'), icon='🦠')
    st.sidebar.page_link('pages/DOC.py', label=_('DOC'), icon='🦠')
    st.sidebar.page_link('pages/Turbidity.py', label=_('Turbidity'), icon='💧')
    st.sidebar.page_link('pages/Lakes_Analysis.py', label=_('Lakes Analysis'), icon='📈')