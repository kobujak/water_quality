# About

The repository contains my master's thesis titled *System for collecting information on the quality of surface waters for selected regions of the United Kingdom using satellite imagery*. Graduated in 2024 at AGH UST.

# Overview

The developed application can be used to assess the quality and condition of surface waters using spectral indexes and water quality parameters such as chlorophyll-a, turbidity, CDOM, and DOC. The study area includes the counties of Cumbria and Hampshire in the United Kingdom.

The Lakes Analysis section presents the results of the calculated calibration coefficient to regionally adjust the algorithm used to calculate DOC using satellite imagery.

The scripts for data processing were written in Python's Jupyter Notebook. The backend of the application utilizes Google Earth Engine Python API and Streamlit.

Streamlit is also responsible for the frontend of the application and its release.

![name](https://github.com/kobujak/water_quality/blob/main/images/NDWI.png)
![name](https://github.com/kobujak/water_quality/blob/main/images/Lakes_point.png)
![name](https://github.com/kobujak/water_quality/blob/main/images/Lakes_calibration.png)

# Data

Sentinel-2 Satellite Imagery - https://developers.google.com/earth-engine/datasets/catalog/sentinel-2
In-situ Dissolved Organic Carbon Measurements (DOC) - https://environment.data.gov.uk/water-quality/view/landing
OSM Water Layer - OSM Water Layer is available for download at the IIS U-Tokyo webpage: http://hydro.iis.u-tokyo.ac.jp/~yamadai/OSM_water/.

# Result

To see the result go to: https://uk-waterquality.streamlit.app/ The application is available in both Polish and English.