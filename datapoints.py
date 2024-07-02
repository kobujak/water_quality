
import ee

def createBuffer(in_df):
    features = []
    for index,row in in_df.iterrows():
        point = ee.Geometry.Point([row['longitude'], row['latitude']])
        buffer = point.buffer(distance = 10)
        feature = ee.Feature(buffer)
        features.append(feature)
    collection = ee.FeatureCollection(features)
    return collection