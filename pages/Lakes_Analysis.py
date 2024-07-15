import geemap.foliumap as geemap
import streamlit as st
import ee
import pandas as pd
from modules.indices import calculateIndex,visualizationParams
from modules.images import getSingleImage
from modules.datapoints import createBuffer
from modules.nav import Navbar
from modules.language import initializeLanguage
import gettext
_ = gettext.gettext



initializeLanguage()
try:
  localizator = gettext.translation('Lakes', localedir='locales', languages=[st.session_state.language])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.set_page_config(page_title=_('Lakes'),layout="wide") # Page config

Navbar() # Sidebar pages



st.title(_('Lakes'))
st.subheader(_('Lakes_description'))

tab1, tab2, tab3, tab4 = st.tabs([_("Lakes_tab"), "Wast Water (NW-88021658)", "Bassenthwaite (NW-88010015)", "Ennerdale Water (NW-88005133)"])

with tab1:
    

    df = pd.read_csv('data_processed.csv', parse_dates = True)

    dates = df['SampleDate'].unique()

    if 'date_lake' not in st.session_state:
        st.session_state.date_lake = dates[0]
        

    with st.form("lakes_form"):
        date_lake = st.select_slider(
        _("Select date"),
        options = dates,
        key = 'date_lake'
        )
        submitted = st.form_submit_button(_("Submit"))
    m = geemap.Map(basemap ='HYBRID')

    selected_df = df.loc[df['SampleDate'] == date_lake]
    m.add_points_from_xy(selected_df, x="longitude", y="latitude")

    img = getSingleImage(st.session_state.date_lake)
    lakes = ee.FeatureCollection("projects/ee-konradbujak09/assets/lakes_analysis", {})
    roi = lakes.geometry()
    doc = calculateIndex(img,"DOC",roi)
    vis = visualizationParams("DOC")
    m.addLayer(doc,vis, "DOC" )
    m.add_colorbar(vis, label="DOC",background_color="#e5e5e5")
    m.addLayer(createBuffer(selected_df),
        {'color': 'red'},
        'Buffer used for calculation')
                
    m.centerObject(doc)
    m.to_streamlit(height=900)


    st.header(_("Selected"))
    st.dataframe(selected_df,use_container_width=True,hide_index=True,column_order=('PointID','Property','Result','Unit','SampleDate','ImageDate','DOC','Turbidity','NDVI','Chlorophyll','CDOM'))
    st.header(_("All"))
    st.dataframe(df,use_container_width=True,hide_index=True,column_order=('PointID','Property','Result','Unit','SampleDate','ImageDate','DOC','Turbidity','NDVI','Chlorophyll','CDOM'))

with tab2:
    st.header("Wast Water (NW-88021658)")
    tab2_df = df.loc[df['PointID'] == 'NW-88021658']
    st.dataframe(tab2_df,use_container_width=True)
    col1, col2 = st.columns(2,gap="medium")

    with col1:
        st.subheader(_("title_measured"))
        st.line_chart(tab2_df, x="SampleDate", y="Result")
        st.subheader(_("title_DOC"))
        st.line_chart(tab2_df, x="ImageDate", y="DOC")
        st.subheader(_("title_CDOM"))
        st.line_chart(tab2_df, x="ImageDate", y="CDOM")
        st.subheader(_("title_Turb"))
        st.line_chart(tab2_df, x="ImageDate", y="Turbidity")
        
    with col2:
        st.subheader(_("title_DOC_calibrated"))
        st.line_chart(tab2_df, x="ImageDate", y="calibratedDOC_ratio")
        st.subheader(_("title_DOC_calibrated_all"))
        st.line_chart(tab2_df, x="SampleDate", y=["Result", "calibratedDOC_ratio","calibratedDOC_reg"], color=["#FF0000", "#0000FF","#00FF00"] )
        st.subheader(_("title_CHLA"))
        st.line_chart(tab2_df, x="ImageDate", y="Chlorophyll")
        st.subheader(_("title_NDVI"))
        st.line_chart(tab2_df, x="ImageDate", y="NDVI")

with tab3:
    st.header("Bassenthwaite (NW-88010015)")
    tab3_df = df.loc[df['PointID'] == 'NW-88010015']
    st.dataframe(tab3_df,use_container_width=True)
    col1, col2 = st.columns(2,gap="medium")

    with col1:
        st.subheader(_("title_measured"))
        st.line_chart(tab3_df, x="SampleDate", y="Result")
        st.subheader(_("title_DOC"))
        st.line_chart(tab3_df, x="ImageDate", y="DOC")
        st.subheader(_("title_CDOM"))
        st.line_chart(tab3_df, x="ImageDate", y="CDOM")
        st.subheader(_("title_Turb"))
        st.line_chart(tab3_df, x="ImageDate", y="Turbidity")

        
    with col2:
        st.subheader(_("title_DOC_calibrated"))
        st.line_chart(tab3_df, x="ImageDate", y="calibratedDOC_ratio")
        st.subheader(_("title_DOC_calibrated_all"))
        st.line_chart(tab3_df, x="SampleDate", y=["Result", "calibratedDOC_ratio","calibratedDOC_reg"], color=["#FF0000", "#0000FF","#00FF00"] )
        st.subheader(_("title_CHLA"))
        st.line_chart(tab3_df, x="ImageDate", y="Chlorophyll")
        st.subheader(_("title_NDVI"))
        st.line_chart(tab3_df, x="ImageDate", y="NDVI")

        

with tab4:
    st.header("Ennerdale Water (NW-88005133)")
    tab4_df = df.loc[df['PointID'] == 'NW-88005133']
    st.dataframe(tab4_df,use_container_width=True)
    col1, col2 = st.columns(2,gap="medium")

    with col1:
        st.subheader(_("title_measured"))
        st.line_chart(tab4_df, x="SampleDate", y="Result")
        st.subheader(_("title_DOC"))
        st.line_chart(tab4_df, x="ImageDate", y="DOC")
        st.subheader(_("title_CDOM"))
        st.line_chart(tab4_df, x="ImageDate", y="CDOM")
        st.subheader(_("title_Turb"))
        st.line_chart(tab4_df, x="ImageDate", y="Turbidity")
        
    with col2:
        st.subheader(_("title_DOC_calibrated"))
        st.line_chart(tab4_df, x="ImageDate", y="calibratedDOC_ratio")
        st.subheader(_("title_DOC_calibrated_all"))
        st.line_chart(tab4_df, x="SampleDate", y=["Result", "calibratedDOC_ratio","calibratedDOC_reg"], color=["#FF0000", "#0000FF","#00FF00"] )
        st.subheader(_("title_CHLA"))
        st.line_chart(tab4_df, x="ImageDate", y="Chlorophyll")
        st.subheader(_("title_NDVI"))
        st.line_chart(tab4_df, x="ImageDate", y="NDVI")

