import ee

def getRoi():
    #to be replaced by correct geometry
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
    return roi