import ee

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

def getImage(roi):
  # parameters for dates should be added
  dataset = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
  image = dataset.filterBounds(roi).filterDate("2020-04-01", "2020-08-01").filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)).sort('CLOUDY_PIXEL_PERCENTAGE',False).map(mask_s2_clouds).mosaic()
  image = image.clip(roi).unmask()

  return image