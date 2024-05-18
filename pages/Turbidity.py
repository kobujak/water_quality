import geemap.foliumap as geemap
import streamlit as st
import ee
from datetime import datetime
from indices import calculateIndex, visualizationParams
from images import getImage
from roi import getRoi
from datapoints import getDatapoints, pointRasterValues

#ee.Authenticate(authorization_code="")

#ee.Initialize()

#page config

st.set_page_config(layout="wide")
st.header('TURBIDITY')

roi = getRoi()

m = geemap.Map(basemap ='CartoDB.DarkMatter')
m.centerObject(roi)

turb = calculateIndex(getImage(roi),"TURBIDITY",roi)
m.addLayer(turb,visualizationParams("TURBIDITY"), "Turbidity" )


points = pointRasterValues(getDatapoints(),turb)
m.add_points_from_xy(points, x="longitude", y="latitude")

m.to_streamlit(height=1000)