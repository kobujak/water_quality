import geemap.foliumap as geemap
import streamlit as st
import ee
from datetime import date,timedelta
from indices import calculateIndex, visualizationParams
from images import getImage
from roi import getRoi
from datapoints import getDatapoints, pointRasterValues


#ee.Authenticate(authorization_code="")

#ee.Initialize()

st.set_page_config(layout="wide")
st.header('TURBIDITY')

roi = getRoi()

m = geemap.Map(basemap ='CartoDB.DarkMatter')
m.centerObject(roi)

if 'dates' not in st.session_state:
    st.session_state.dates = (date(2023, 4, 1),date(2023, 4, 30))


turb = calculateIndex(getImage(start = st.session_state.dates[0], end = st.session_state.dates[1],roi = roi),"TURBIDITY",roi)
m.addLayer(turb,visualizationParams("TURBIDITY"), "Turbidity" )

points = pointRasterValues(getDatapoints(start = st.session_state.dates[0], end = st.session_state.dates[1]),turb)
m.add_points_from_xy(points, x="longitude", y="latitude")

m.to_streamlit(height=1000)

# def on_slider_click():
#     st.session_state.dates

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

