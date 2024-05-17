import pandas as pd
import streamlit as st

data = pd.read_csv('CL-2023-M.csv')
data = data[['sample.samplingPoint.notation','determinand.label','determinand.notation','result','determinand.unit.label']]
df = data.loc[data['determinand.notation'] == 6396]

st.table(df)