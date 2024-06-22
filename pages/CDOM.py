import geemap.foliumap as geemap
import streamlit as st
import ee
from datetime import date,timedelta
from indices import calculateIndex, visualizationParams
from images import getImage
from roi import getRoi

#ee.Authenticate(authorization_code="")

ee.Initialize()
if 'dates_cdom' not in st.session_state:
    st.session_state.dates_cdom = (date(2023, 4, 1),date(2023, 4, 30))
#page config

st.set_page_config(layout="wide")
st.header('CDOM')

roi = getRoi()

m = geemap.Map(basemap ='HYBRID')
m.centerObject(roi)

m.addLayer(calculateIndex(getImage(st.session_state.dates_cdom[0],st.session_state.dates_cdom[1],roi,sr=False),"CDOM",),visualizationParams("CDOM"), "CDOM" )
m.to_streamlit(height=1000)


with st.form("my_form"):
   dates_cdom = st.slider(
        "Select date range",
        format = "YYYY-MM-DD ",
        step = timedelta(days=6),
        min_value = date(2018, 4, 1),
        max_value = date.today(),
        key = 'dates_cdom'
        )
   submitted = st.form_submit_button("Submit")