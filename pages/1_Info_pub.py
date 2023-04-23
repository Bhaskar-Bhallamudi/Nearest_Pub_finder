import streamlit as st
import numpy as np
import pandas 
from PIL import Image
import os


st.header('Pubs info ')
image = Image.open(r'C:\Users\bhask\Desktop\DATA SCIENCE AND ANALYTICS\Internship_Inno\FLASK\Pub_Nearest_project\resources\pubs_by_location.png')
st.image(image, use_column_width= True)

image_2 = Image.open(r'C:\Users\bhask\Desktop\DATA SCIENCE AND ANALYTICS\Internship_Inno\FLASK\Pub_Nearest_project\resources\pubs_vs_local_authorities.png')
st.image(image_2, use_column_width= True)