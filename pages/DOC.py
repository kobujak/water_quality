import geemap.foliumap as geemap
import streamlit as st
import ee
from datetime import date,timedelta
from indices import calculateIndex,visualizationParams
from images import getImage
from roi import getRoi
from datapoints import getDatapoints, pointRasterValues

#ee.Authenticate(authorization_code="")

ee.Initialize()
if 'dates_doc' not in st.session_state:
    st.session_state.dates_doc = (date(2023, 4, 1),date(2023, 4, 30))
#page config

st.set_page_config(layout="wide")
st.header('DOC')

roi = getRoi()

m = geemap.Map(basemap ='HYBRID')
m.centerObject(roi)

doc = calculateIndex(getImage(st.session_state.dates_doc[0],st.session_state.dates_doc[1],roi,sr=False),"DOC")
m.addLayer(doc,visualizationParams("DOC"), "DOC" )

points = pointRasterValues(getDatapoints(st.session_state.dates_doc[0],st.session_state.dates_doc[1],'0301'),doc)
m.add_points_from_xy(points, x="longitude", y="latitude")

m.to_streamlit(height=1000)


with st.form("my_form"):
   dates_doc = st.slider(
        "Select date range",
        format = "YYYY-MM-DD ",
        step = timedelta(days=6),
        min_value = date(2018, 4, 1),
        max_value = date.today(),
        key = 'dates_doc'
        )
   submitted = st.form_submit_button("Submit")
