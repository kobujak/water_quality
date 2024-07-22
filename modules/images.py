import ee
from datetime import  datetime, timedelta

def mask_clouds(img):
  qa_band = 'cs_cdf'
  clear_treshold = 0.65
  return img.updateMask(img.select(qa_band).gte(clear_treshold))


def getImage(start,end, roi, sr=True):

  start = start.strftime('%Y-%m-%d')
  end = end.strftime('%Y-%m-%d')
  if sr == True:
    s2 = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
  else:
    s2 = ee.ImageCollection("COPERNICUS/S2_HARMONIZED")

  csPlus = ee.ImageCollection('GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED')

  qa_band = 'cs_cdf'

  image = s2.filterBounds(roi).filterDate(start, end).linkCollection(csPlus, [qa_band]).map(mask_clouds).median()
  image = image.clip(roi)

  return image.divide(10000)

def getSingleImage(date, sr=True):

  feature = ee.FeatureCollection("projects/ee-konradbujak09/assets/lakes_analysis", {})
  roi = feature.geometry()

  start_date = datetime.strptime(date, '%Y-%m-%d') - timedelta(days=4)
  end_date = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=4)
  start_date = start_date.strftime('%Y-%m-%d')
  end_date = end_date.strftime('%Y-%m-%d')

  csPlus = ee.ImageCollection('GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED')

  qa_band = 'cs_cdf'

  if sr == True:
    s2 = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
  else:
    s2 = ee.ImageCollection("COPERNICUS/S2_HARMONIZED")

  img = s2 \
    .filterBounds(roi). \
    filterDate(start_date, end_date) \
    .linkCollection(csPlus, [qa_band]).map(mask_clouds)\
    .sort('CLOUDY_PIXEL_PERCENTAGE').first()
  img = img.clip(roi)
  return img.divide(10000)
