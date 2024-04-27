#import ee

def calculateIndex(image,index):
    ndwi = image.normalizedDifference(["B3", "B8"])
    if index.upper() == "NDWI":
        result = ndwi
    elif index.upper() == "NDTI":
        watermask = ndwi.gt(0)
        ndti = image.normalizedDifference(["B4", "B3"])
        result = ndti.updateMask(watermask)
    elif index.upper() == "TURBIDITY":
        watermask = ndwi.gt(0)
        turbidity = image.expression(
        '8.93 * (GREEN/AERO) - 6.39', {
        'AERO': image.select('B1'),
        'GREEN': image.select('B3')})
        result = turbidity.updateMask(watermask)
    elif index.upper() == "CHLA":
        watermask = ndwi.gt(0)
        turbidity = image.expression(
        '4.26 * pow(1.0*(GREEN/AERO), 3.94)', {
        'AERO': image.select('B1'),
        'GREEN': image.select('B3')})
        result = turbidity.updateMask(watermask)
    elif index.upper() == "CYA":
        watermask = ndwi.gt(0)
        turbidity = image.expression(
        '115530.31 * pow(GREEN * (RED / BLUE), 2.38)', {
        'BLUE': image.select('B2'),
        'GREEN': image.select('B3'),
        'RED': image.select('B4')})
        result = turbidity.updateMask(watermask)
    elif index.upper() == "CDOM":
        watermask = ndwi.gt(0)
        turbidity = image.expression(
        '537 * exp(-2.93*GREEN/RED)', {
        'GREEN': image.select('B3'),
        'RED': image.select('B4')})
        result = turbidity.updateMask(watermask)
    elif index.upper() == "DOC":
        watermask = ndwi.gt(0)
        turbidity = image.expression(
        '432 * exp(-2.24*GREEN/RED)', {
        'GREEN': image.select('B3'),
        'RED': image.select('B4')})
        result = turbidity.updateMask(watermask)
    else:
        result = 0
    
    return result



def visualizationParams(index):
    if index.upper() == 'RGB':
        vis = {"bands": ["B4", "B3", "B2"],'min': 0.0,'max': 0.3}
    elif index.upper() == "NDWI":
        vis = {'min': -1, 'max': 1, 'palette': ['00FFFF', '0000FF']}       
    elif index.upper() == "NDTI":
         vis = {'min': -1, 'max': 0, 'palette': ['f22f11', 'ebd510','0af50a']}
    elif index.upper() == "TURBIDITY":
         vis = {'min': 0, 'max': 20, 'palette': ['f22f11', 'ebd510','0af50a']}
    elif index.upper() == "CHLA":
         vis = {'min': 0, 'max': 50, 'palette': ['f22f11', 'ebd510','0af50a']}
    elif index.upper() == "CYA":
         vis = {'min': 0, 'max': 100, 'palette': ['f22f11', 'ebd510','0af50a']}
    elif index.upper() == "CDOM":
         vis = {'min': 0, 'max': 5, 'palette': ['f22f11', 'ebd510','0af50a']}
    elif index.upper() == "DOC":
         vis = {'min': 0, 'max': 40, 'palette': ['f22f11', 'ebd510','0af50a']}
    else:
         vis = {}                
    return vis
