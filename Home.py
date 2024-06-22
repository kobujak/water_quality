import geemap.foliumap as geemap
import streamlit as st
import ee
from datetime import date,timedelta
from indices import calculateIndex, visualizationParams
from images import getImage
from roi import getRoi

ee.Initialize()

#page config
st.set_page_config(layout="wide")
st.header('Water quality')

st.write("There will be text")

if 'dates' not in st.session_state:
    st.session_state.dates = (date(2023, 4, 1),date(2023, 4, 30))

roi = getRoi()

m = geemap.Map()
m.centerObject(roi)

m.addLayer(getImage(start = st.session_state.dates[0], end = st.session_state.dates[1],roi = roi),visualizationParams("RGB"), "RGB" )

m.to_streamlit(height=1000)

with st.form("my_form"):
   dates = st.slider(
        "Select date range",
        format = "YYYY-MM-DD ",
        step = timedelta(days=10),
        min_value = date(2018, 1, 1),
        max_value = date.today(),
        key = 'dates'
        )
   submitted = st.form_submit_button("Submit")



