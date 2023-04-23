import streamlit as st
import os
from PIL import Image


st.title("Welcome to the Pub finder !!! Have a nice day")

st.header('Top 15 locations with most pubs')
image = Image.open(r'C:\Users\bhask\Desktop\DATA SCIENCE AND ANALYTICS\Internship_Inno\FLASK\Pub_Nearest_project\resources\pubs_by_location.png')
st.image(image, use_column_width= True)