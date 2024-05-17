import ee

def getRoi():
    feature = ee.FeatureCollection("projects/ee-konradbujak09/assets/ROI", {})
    roi = feature.geometry()
    return roi