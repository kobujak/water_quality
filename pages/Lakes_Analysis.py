import geemap.foliumap as geemap
import streamlit as st
import ee
import pandas as pd
from indices import calculateIndex,visualizationParams
from images import getSingleImage
from datapoints import createBuffer



st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["Lakes", "Wast Water (NW-88021658)", "Bassenthwaite (NW-88010015)", "Ennerdale Water (NW-88005133)"])

with tab1:
    col1, col2 = st.columns(2,gap="medium")

    df = pd.read_csv('2024-06-05.csv', parse_dates = True)

    dates = df['SampleDate'].unique()

    if 'date_lake' not in st.session_state:
        st.session_state.date_lake = dates[0]

    with col1:
        st.header("Map")

        with st.form("my_form"):
            date_lake = st.select_slider(
            "Select date ",
            options = dates,
            value = dates[0],
            key = 'date_lake'
            )
            submitted = st.form_submit_button("Submit")
        m = geemap.Map()

        selected_df = df.loc[df['SampleDate'] == date_lake]
        m.add_points_from_xy(selected_df, x="longitude", y="latitude")

        img = getSingleImage(st.session_state.date_lake)
        lakes = ee.FeatureCollection("projects/ee-konradbujak09/assets/lakes_analysis", {})
        roi = lakes.geometry()
        doc = calculateIndex(img,"DOC",roi)

        m.addLayer(img,visualizationParams("RGB"), "RGB" )
        m.addLayer(doc,visualizationParams("DOC"), "DOC" )
        m.addLayer(createBuffer(selected_df),
             {'color': 'red'},
             'Buffer used for calculation')

        
        m.centerObject(doc)
        m.to_streamlit(height=700)

    with col2:
        st.header("Selected Points")
        st.dataframe(selected_df,width=900)
        st.header("All points")
        st.dataframe(df,width=900)

with tab2:
    col1, col2 = st.columns(2,gap="medium")
    with col1:
        st.header("Wast Water (NW-88021658)")
        tab2_df = df.loc[df['PointID'] == 'NW-88021658']
        st.subheader("Measured values")
        st.line_chart(tab2_df, x="SampleDate", y="Result")
        st.subheader("Values calculated from raster")
        st.line_chart(tab2_df, x="ImageDate", y="DOC")
        st.line_chart(tab2_df, x="SampleDate", y=["Result", "DOC"], color=["#FF0000", "#0000FF"] )
    with col2:
        st.dataframe(tab2_df,width=900)

with tab3:
    col1, col2 = st.columns(2,gap="medium")
    with col1:
        st.header("Bassenthwaite (NW-88010015)")
        tab3_df = df.loc[df['PointID'] == 'NW-88010015']
        st.subheader("Measured values")
        st.line_chart(tab3_df, x="SampleDate", y="Result")
        st.subheader("Values calculated from raster")
        st.line_chart(tab3_df, x="ImageDate", y="DOC")
        st.line_chart(tab3_df, x="SampleDate", y=["Result", "DOC"], color=["#FF0000", "#0000FF"] )
    with col2:
        st.dataframe(tab2_df,width=900)

with tab4:
    col1, col2 = st.columns(2,gap="medium")
    with col1:
        st.header("Ennerdale Water (NW-88005133)")
        tab4_df = df.loc[df['PointID'] == 'NW-88005133']
        st.subheader("Measured values")
        st.line_chart(tab4_df, x="SampleDate", y="Result")
        st.subheader("Values calculated from raster")
        st.line_chart(tab4_df, x="ImageDate", y="DOC")
        st.line_chart(tab4_df, x="SampleDate", y=["Result", "DOC"], color=["#FF0000", "#0000FF"] )
        with col2:
            st.dataframe(tab2_df,width=900)

