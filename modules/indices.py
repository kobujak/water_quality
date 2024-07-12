import ee
from modules.roi import getRoi

def calculateIndex(image,index,roi_water = None):
        
    if index.upper() == "NDWI":
        ndwi = image.normalizedDifference(["B3", "B8"])
        result = ndwi
    elif index.upper() == "NDTI":
        ndti = image.normalizedDifference(["B4", "B3"])
        result = ndti
    elif index.upper() == "NDVI":
        ndvi = image.normalizedDifference(["B5", "B4"])
        result = ndvi
    elif index.upper() == "TURBIDITY":
        turbidity = image.expression(
        '8.93 * (GREEN/AERO) - 6.39', {
        'AERO': image.select('B1'),
        'GREEN': image.select('B3')})
        result = turbidity
    elif index.upper() == "CHLA":
        chla = image.expression(
        '4.26 * pow(1.0*(GREEN/AERO), 3.94)', {
        'AERO': image.select('B1'),
        'GREEN': image.select('B3')})
        result = chla
    elif index.upper() == "CYA":
        cya = image.expression(
        '115530.31 * pow(GREEN * (RED / BLUE), 2.38)', {
        'BLUE': image.select('B2'),
        'GREEN': image.select('B3'),
        'RED': image.select('B4')})
        result = cya
    elif index.upper() == "CDOM":
        cdom = image.expression(
        '537 * exp(-2.93*GREEN/RED)', {
        'GREEN': image.select('B3'),
        'RED': image.select('B4')})
        result = cdom
    elif index.upper() == "DOC":
        doc = image.expression(
        '432 * exp(-2.24*GREEN/RED)', {
        'GREEN': image.select('B3'),
        'RED': image.select('B4')})
        result = doc
    else:
        result = 0
    
    if roi_water is None:
        roi = getRoi()
        osm_water = ee.ImageCollection("projects/sat-io/open-datasets/OSM_waterLayer").median().clip(roi)
        mask = osm_water.select('b1').eq(2).Or(osm_water.select('b1').eq(3))
        watermask = osm_water.updateMask(mask)
        result = result.updateMask(watermask)
    else:
        result = result.clip(roi_water)

    return result



def visualizationParams(index):
    
    if index.upper() == 'RGB':
        vis = {"bands": ["B4", "B3", "B2"],'min': 0.0,'max': 2500}
    elif index.upper() == "NDWI":
        vis = {'min': -1, 'max': 1, 'palette': ['00FFFF', '0000FF']}       
    elif index.upper() == "NDTI":
         vis = {'min': -1, 'max': 0, 'palette': ['0af50a', 'ebd510','f22f11']}
    elif index.upper() == "NDVI":
         vis = {'min': -1, 'max': 1, 'palette': ['f22f11', 'ebd510','0af50a']}    
    elif index.upper() == "TURBIDITY":
         vis =  {'min': 0, 'max': 20, 'palette': ['496FF2','82D35F','FEFD05', 'FD0004','8E7C26','D97CF5']}
    elif index.upper() == "CHLA":
         vis = {'min': 0, 'max': 50, 'palette': ['496FF2','82D35F','FEFD05', 'FD0004','8E7C26','D97CF5']}
    elif index.upper() == "CYA":
         vis =  {'min': 0, 'max': 100, 'palette': ['496FF2','82D35F','FEFD05', 'FD0004','8E7C26','D97CF5']}
    elif index.upper() == "CDOM":
         vis =  {'min': 0, 'max': 5, 'palette': ['496FF2','82D35F','FEFD05', 'FD0004','8E7C26','D97CF5']}
    elif index.upper() == "DOC":
         vis = {'min': 0, 'max': 40, 'palette': ['496FF2','82D35F','FEFD05', 'FD0004','8E7C26','D97CF5']}
    else:
         vis = {}                
    return vis
