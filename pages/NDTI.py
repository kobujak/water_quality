import geemap.foliumap as geemap
import streamlit as st
import ee
from datetime import date,timedelta
from indices import calculateIndex, visualizationParams
from images import getImage
from roi import getRoi
from modules.nav import Navbar

#ee.Authenticate(authorization_code="")

st.set_page_config(layout="wide") # Page config

Navbar() # Sidebar pages
ee.Initialize()
st.title('NDTI')

ee.Initialize()

if 'dates_ndti' not in st.session_state:
    st.session_state.dates_ndti = (date(2023, 4, 1),date(2023, 4, 30))

roi = getRoi()

m = geemap.Map(basemap ='HYBRID')
m.centerObject(roi)

m.addLayer(calculateIndex(getImage(st.session_state.dates_ndti[0],st.session_state.dates_ndti[1],roi),"NDTI"),visualizationParams("NDTI"), "NDTI" )
m.to_streamlit(height=1000)


with st.form("my_form"):
   dates_ndti = st.slider(
        "Select date range",
        format = "YYYY-MM-DD ",
        step = timedelta(days=6),
        min_value = date(2018, 4, 1),
        max_value = date.today(),
        key = 'dates_ndti'
        )
   submitted = st.form_submit_button("Submit")