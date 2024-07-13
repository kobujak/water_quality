import ee
import geemap

def getRoi():
    geemap.ee_initialize()
    feature = ee.FeatureCollection("projects/ee-konradbujak09/assets/ROI_CU_HMP", {})
    roi = feature.geometry()
    return roi