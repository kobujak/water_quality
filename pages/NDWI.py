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
  localizator = gettext.translation('NDWI', localedir='locales', languages=[st.session_state.language])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.set_page_config(page_title=_('NDWI_title'),layout="wide") # Page config



if 'dates_ndwi' not in st.session_state:
    st.session_state.dates_ndwi = (date(2023, 4, 1),date(2023, 4, 30))

Navbar() # Sidebar pages
st.title(_('NDWI_title'))
st.subheader(_('NDWI_description'))

roi = getRoi()

m = geemap.Map(basemap ='HYBRID')
m.centerObject(roi)
vis = visualizationParams("NDWI")
m.addLayer(calculateIndex(getImage(st.session_state.dates_ndwi[0],st.session_state.dates_ndwi[1],roi),"NDWI"),vis, "NDWI" )
m.add_colorbar(vis, label="NDWI",background_color="#e5e5e5")
m.to_streamlit(height=900)


with st.form("ndwi_form"):
   dates_ndwi = st.slider(
        _("Select date range"),
        format = "YYYY-MM-DD ",
        step = timedelta(days=6),
        min_value = date(2018, 4, 1),
        max_value = date.today(),
        key = 'dates_ndwi'
        )
   submitted = st.form_submit_button(_("Submit"))