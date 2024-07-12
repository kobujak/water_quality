import geemap.foliumap as geemap
import streamlit as st
import ee
from datetime import date,timedelta
from modules.indices import calculateIndex, visualizationParams
from modules.images import getImage
from modules.roi import getRoi
from modules.nav import Navbar
from modules.language import initializeLanguage
import gettext
_ = gettext.gettext

#ee.Authenticate(authorization_code="")
initializeLanguage()
try:
  localizator = gettext.translation('NDVI', localedir='locales', languages=[st.session_state.language])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.set_page_config(page_title=_('NDVI_title'),layout="wide") # Page config


ee.Initialize()

if 'dates_ndvi' not in st.session_state:
    st.session_state.dates_ndvi = (date(2023, 4, 1),date(2023, 4, 30))

Navbar() # Sidebar pages
st.title(_('NDVI_title'))
st.subheader(_('NDVI_description'))

roi = getRoi()

m = geemap.Map(basemap ='HYBRID')
m.centerObject(roi)

m.addLayer(calculateIndex(getImage(st.session_state.dates_ndvi[0],st.session_state.dates_ndvi[1],roi),"NDVI"),visualizationParams("NDVI"), "NDVI" )
m.to_streamlit(height=900)


with st.form("ndvi_form"):
   dates_ndvi = st.slider(
        _("Select date range"),
        format = "YYYY-MM-DD ",
        step = timedelta(days=6),
        min_value = date(2018, 4, 1),
        max_value = date.today(),
        key = 'dates_ndvi'
        )
   submitted = st.form_submit_button(_("Submit"))