import pandas as pd
import requests
import streamlit as st
import ee

#@st.cache_data()
def getDatapoints(start,end,det): 
    
    headers = requests.utils.default_headers()

    headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
    )

    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')

    baseurl = 'http://environment.data.gov.uk/water-quality' 
    pathHS = baseurl + '/data/measurement?determinand='+det+'&_limit=100&startDate='+start+'&endDate='+end+'&subArea=10-39-K&_view=full'
    pathCL = baseurl + '/data/measurement?determinand='+det+'&_limit=100&startDate='+start+'&endDate='+end+'&subArea=4-11-B&_view=full'
    urls = [pathHS,pathCL]

    data = []
    for url in urls:
        response = requests.get(url,headers=headers) 
        if response.status_code == 200:
            response_json = response.json()
            response_json = pd.json_normalize(response_json['items'])
            df = pd.DataFrame(response_json)
            df = df[['determinand.label','result','determinand.unit.label','sample.samplingPoint.lat','sample.samplingPoint.long','sample.sampleDateTime']]
            df.rename(columns={'determinand.label': 'label', 'determinand.unit.label': 'unit', 'sample.samplingPoint.lat': 'latitude', 'sample.samplingPoint.long': 'longitude','sample.sampleDateTime':'SampleDate'}, inplace=True)
            data.append(df)
    return pd.concat(data)

def pointRasterValues(in_df,img):
    
    
    in_df = in_df.sort_values(by=['SampleDate'])
    in_df.insert(0,'MY_ID',range(0,len(in_df)))

    features = []
    rasterValue = []
    Indexes = []
    for index,row in in_df.iterrows():
        point = ee.Geometry.Point([row['longitude'], row['latitude']])
        buffer = point.buffer(distance = 10)
        properties = dict(row)
        feature = ee.Feature(buffer, properties)
        features.append(feature)
        collection = ee.FeatureCollection(features)

        stats = img.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=collection,
        scale=10,  # meters
        )
        rasterValue.append(stats.get('constant').getInfo())
        Indexes.append(row['MY_ID'])




    d = {'MY_ID': Indexes, 'constant': rasterValue}
    values = pd.DataFrame(d)
    result = pd.merge(in_df, values.set_index('MY_ID'), left_on= 'MY_ID',
                   right_index= True, 
                   how = 'left')
    result = result.drop('MY_ID', axis=1)
    return result

def createBuffer(in_df):
    features = []
    for index,row in in_df.iterrows():
        point = ee.Geometry.Point([row['longitude'], row['latitude']])
        buffer = point.buffer(distance = 10)
        feature = ee.Feature(buffer)
        features.append(feature)
    collection = ee.FeatureCollection(features)
    return collection