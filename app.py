import streamlit as st
import rasterio
from utils import arrayToImage
import cv2
import numpy as np
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw

st.set_page_config(page_title='GeoJSON Creator', layout="wide")

st.header("Upload True Color Tiff file")
inputid = st.text_input("Enter ID 👇")
file = st.file_uploader("Choose a file", type=['tiff','tif'])

if file is not None:
    rgbfile = rasterio.open(file)
    rgb = rgbfile.read()
    bounds = rgbfile.bounds
    image = np.clip(rgb, a_min=0, a_max=0.4)
    image = arrayToImage(rgb)
    filename = "./input"+str(inputid)+".png"
    cv2.imwrite(filename, image)
    map = folium.Map(location=[bounds[1], bounds[0]], zoom_start=16, scrollWheelZoom=True, tiles='CartoDB positron')
    img = folium.raster_layers.ImageOverlay(
        name="RGB Image",
        image=filename,
        bounds=[[bounds[1], bounds[0]], [bounds[3], bounds[2]]],
        opacity=1.0,
        interactive=True,
        cross_origin=False,
        zindex=1,
    )
    img.add_to(map)
    draw = Draw(export=True)
    draw.add_to(map)
    st_map = st_folium(map, width=1000, height=650)