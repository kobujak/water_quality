import geemap.foliumap as geemap
import streamlit as st
from datetime import date,timedelta
from modules.indices import calculateIndex, visualizationParams
from modules.images import getImage
from modules.roi import getRoi
from modules.nav import Navbar
from modules.language import initializeLanguage
import gettext
_ = gettext.gettext

initializeLanguage()
try:
  localizator = gettext.translation('cdom', localedir='locales', languages=[st.session_state.language])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.set_page_config(page_title=_('CDOM_title'),layout="wide") # Page config



if 'dates_cdom' not in st.session_state:
    st.session_state.dates_cdom = (date(2023, 4, 1),date(2023, 4, 30))

Navbar() # Sidebar pages
st.title(_('CDOM_title'))
st.subheader(_('CDOM_text'))

roi = getRoi()

m = geemap.Map(basemap ='HYBRID')
m.centerObject(roi)

m.addLayer(calculateIndex(getImage(st.session_state.dates_cdom[0],st.session_state.dates_cdom[1],roi,sr=False),"CDOM",),visualizationParams("CDOM"), "CDOM" )
m.to_streamlit(height=900)

with st.form("cdom_form"):
   dates_chla = st.slider(
        _("Select date range"),
        format = "YYYY-MM-DD ",
        step = timedelta(days=6),
        min_value = date(2018, 4, 1),
        max_value = date.today(),
        key = 'dates_cdom'
        )
   submitted = st.form_submit_button(_("Submit"))