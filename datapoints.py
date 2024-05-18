import pandas as pd
import requests
import streamlit as st
import ee

@st.cache_data()
def getDatapoints(): #TODO dates parameters
    
    headers = requests.utils.default_headers()

    headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
    )

    baseurl = 'http://environment.data.gov.uk/water-quality' 
    pathHS = baseurl + '/data/measurement?determinand=6396&_limit=100&startDate=2023-01-01&endDate=2023-12-31&subArea=10-39-K&_view=full'
    pathCL = baseurl + '/data/measurement?determinand=6396&_limit=100&startDate=2023-01-01&endDate=2023-12-31&area=4-11&_view=full'
    urls = [pathHS,pathCL]

    data = []
    for url in urls:
        response = requests.get(url,headers=headers) 
        if response.status_code == 200:
            response_json = response.json()
            response_json = pd.json_normalize(response_json['items'])
            df = pd.DataFrame(response_json)
            df = df[['determinand.label','result','determinand.unit.label','sample.samplingPoint.lat','sample.samplingPoint.long']]
            df.rename(columns={'determinand.label': 'label', 'determinand.unit.label': 'unit', 'sample.samplingPoint.lat': 'latitude', 'sample.samplingPoint.long': 'longitude'}, inplace=True)
            data.append(df)
    return pd.concat(data)

def pointRasterValues(in_df,img):
    


    features = []
    for index,row in in_df.iterrows():
        geometry = ee.Geometry.Point([row['longitude'], row['latitude']])
        properties = dict(row)
        feature = ee.Feature(geometry, properties)
        features.append(feature)
    collection = ee.FeatureCollection(features)

    results = img.sampleRegions(
        collection = collection,
        scale = 10
    )

    first = results.first().getInfo()
    columns = list(first['properties'].keys())
    points_list = results.reduceColumns(ee.Reducer.toList(len(columns)), columns).values().get(0)
    new_rows = points_list.getInfo()
    new_df = pd.DataFrame(new_rows,columns = columns)
    new_df.rename(columns={'constant': 'RasterValue'}, inplace=True)
    return new_df