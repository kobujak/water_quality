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
if 'dates_tr' not in st.session_state:
    st.session_state.dates_tr = (date(2023, 4, 1),date(2023, 4, 30))

st.set_page_config(layout="wide")
st.header('TURBIDITY')

roi = getRoi()

m = geemap.Map(basemap ='HYBRID')
m.centerObject(roi)

turb = calculateIndex(getImage(st.session_state.dates_tr[0],st.session_state.dates_tr[1],roi),"TURBIDITY")
m.addLayer(turb,visualizationParams("TURBIDITY"), "Turbidity" )

points = pointRasterValues(getDatapoints(st.session_state.dates_tr[0], st.session_state.dates_tr[1],'6396'),turb)
m.add_points_from_xy(points, x="longitude", y="latitude")

m.to_streamlit(height=700)


with st.form("my_form"):
   dates_tr = st.slider(
        "Select date range",
        format = "YYYY-MM-DD ",
        step = timedelta(days=6),
        min_value = date(2018, 4, 1),
        max_value = date.today(),
        key = 'dates_tr'
        )
   submitted = st.form_submit_button("Submit")

