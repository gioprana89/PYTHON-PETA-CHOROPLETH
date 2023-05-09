import pandas as pd
import numpy as np
import folium
import geopandas as gdp
import geopandas as geopandas
import json
import requests
import streamlit as st
import folium as folium 
import pandas as pd
from streamlit_folium import st_folium

st.set_page_config(layout="wide")





st.markdown("<h5 style='text-align: justify; color: blue;'>Membuat Peta dengan Python (Library: STREAMLIT & FOLIUM)<br><br></h5>", unsafe_allow_html=True)

st.image("ugi.png", caption='', width = 350)


#shp_indonesia = gdp.read_file('D:/PYTHON/STREAMLIT/PETA/FOLIUM/MEMBERI WARNA DAN LABEL PADA PETA/untuk streamlit/sumatera_shp_new.shp')
shp_indonesia = gdp.read_file('sumatera_shp_new.shp') #untuk deploy


gdf = geopandas.GeoDataFrame(shp_indonesia, crs="EPSG:4326")

hasil_gjson_id = gdf.to_json()


#data_csv = pd.read_csv("D:/PYTHON/STREAMLIT/PETA/FOLIUM/MEMBERI WARNA DAN LABEL PADA PETA/untuk streamlit/data_csv.csv")
data_csv = pd.read_csv("data_csv.csv") #untuk deploy


ekstrak_data = data_csv[['NAME_1','jumlah']]




#geo_json_data = json.load(open('D:/PYTHON/STREAMLIT/PETA/FOLIUM/MEMBERI WARNA DAN LABEL PADA PETA/untuk streamlit/sumatera_gsjon.geojson', 'r'))
geo_json_data = json.load(open('sumatera_gsjon.geojson', 'r')) #untuk deploy



m = folium.Map([3.597031, 98.678513], tiles="cartodbpositron", zoom_start=6)


tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']

for tile in tiles:
 folium.TileLayer(tile).add_to(m)

choropleth = folium.Choropleth(
    geo_data = geo_json_data,
      name = 'choropleth', 
    data = ekstrak_data,
    columns=['NAME_1','jumlah'],   
    key_on="feature.properties.NAME_1",
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    highlight = True
).add_to(m)


folium.LayerControl().add_to(m)

choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['NAME_1','jumlah'], labels=False)
)



st_data = st_folium(m, width = "100%")




