import geemap.foliumap as geemap
import streamlit as st
import ee
from indices import calculateIndex,visualizationParams
from images import getImage
from roi import getRoi

#ee.Authenticate(authorization_code="")

ee.Initialize()

#page config

st.set_page_config(layout="wide")
st.header('CHLA')

roi = getRoi()

m = geemap.Map()
m.centerObject(roi)

m.addLayer(calculateIndex(getImage(roi),"CHLA",roi),visualizationParams("CHLA"), "CHLA" )
m.to_streamlit(height=1000)