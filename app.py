import geemap.foliumap as geemap
import streamlit as st
import ee
from indices import calculateIndex,visualizationParams

#ee.Authenticate(authorization_code="")

def mask_s2_clouds(image):
  """Masks clouds in a Sentinel-2 image using the QA band.

  Args:
      image (ee.Image): A Sentinel-2 image.

  Returns:
      ee.Image: A cloud-masked Sentinel-2 image.
  """
  qa = image.select('QA60')

  # Bits 10 and 11 are clouds and cirrus, respectively.
  cloud_bit_mask = 1 << 10
  cirrus_bit_mask = 1 << 11

  # Both flags should be set to zero, indicating clear conditions.
  mask = (
      qa.bitwiseAnd(cloud_bit_mask)
      .eq(0)
      .And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
  )

  return image.updateMask(mask).divide(10000)


st.set_page_config(layout="wide")
st.header('Water quality')

st.subheader('NDTI')

m = geemap.Map()
dataset = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
geom = ee.Geometry.Polygon(
        [
            [
                [-3.351026, 51.680276],
                [-3.351026, 52.450207],
                [-1.944798, 52.450207],
                [-1.944798, 51.680276],
                [-3.351026, 51.680276],
            ]
        ]
    )
feature = ee.Feature(geom, {})

roi = feature.geometry()
m.centerObject(roi)

image = dataset.filterBounds(roi).filterDate("2020-04-01", "2020-08-01").filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)).sort('CLOUDY_PIXEL_PERCENTAGE',False).map(mask_s2_clouds).mosaic()
image = image.clip(roi).unmask()

m.addLayer(image, visualizationParams("RGB"), "RGB_img")
m.addLayer(calculateIndex(image,"NDTI",roi),visualizationParams("NDTI"), "NDTI" )
m.addLayer(calculateIndex(image,"TURBIDITY",roi),visualizationParams("TURBIDITY"), "TURBIDITY" )
m.addLayer(calculateIndex(image,"CHLA",roi),visualizationParams("CHLA"), "CHLA" )
m.addLayer(calculateIndex(image,"CYA",roi),visualizationParams("CYA"), "CYA" )
m.addLayer(calculateIndex(image,"CDOM",roi),visualizationParams("CDOM"), "CDOM" )
m.addLayer(calculateIndex(image,"DOC",roi),visualizationParams("DOC"), "DOC" )

m.to_streamlit(height=1000)

