import ee

def getRoi():
    feature = ee.FeatureCollection("projects/ee-konradbujak09/assets/ROI_CU_HMP", {})
    roi = feature.geometry()
    return roi