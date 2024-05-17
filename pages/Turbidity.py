import geemap.foliumap as geemap
import streamlit as st
import ee
from indices import calculateIndex,visualizationParams
from images import getImage
from roi import getRoi
from datapoints import getDatapoints

#ee.Authenticate(authorization_code="")

#ee.Initialize()

#page config

st.set_page_config(layout="wide")
st.header('TURBIDITY')

roi = getRoi()

m = geemap.Map(basemap ='CartoDB.DarkMatter')
m.centerObject(roi)

m.addLayer(calculateIndex(getImage(roi),"TURBIDITY",roi),visualizationParams("TURBIDITY"), "Turbidity" )

points = getDatapoints()
m.add_points_from_xy(points, x="longitude", y="latitude")

m.to_streamlit(height=1000)