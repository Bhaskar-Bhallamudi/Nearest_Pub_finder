import numpy as np
import pandas as pd
import streamlit as st


st.header('Nearest Pub')

# loading the data
df = pd.read_csv(r"C:\Users\bhask\Desktop\DATA SCIENCE AND ANALYTICS\Internship_Inno\FLASK\Pub_Nearest_project\resources\open_pubs_cleaned.csv")

# taking input
lat,long=st.columns(2)
with lat:
    lat=st.number_input(label="Enter Latitude coordinates", min_value=49.892485, max_value=60.764969)
with long:
    long=st.number_input(label="Enter Longitude coordinates", min_value=-7.384525, max_value=1.757763)


#selected coordinates
search_coor = np.array((lat,long))

#available 
available_coor = np.array([df['latitude'],df['longitude']]).T

# finding euclidean distance
distance=np.sum((available_coor-search_coor)**2, axis=1)

#Adding Distance column to dataframe
df['Distance_new']=distance

#Asking user that how many nearest Pub they want to see
#nearest=st.slider(label="How Many Nearest Pub You Want to See", min_value=1, max_value=50, value=5)
data=df.sort_values(by='Distance_new', ascending=True)[ :15]

#List of Bar Names
st.subheader(f"15 Nearest Pubs:")

#Show Nearest Pubs on Map
st.map(data=data, zoom=None, use_container_width=True)

#Name and Address of Nearby Pubs
st.table(data[['name','address','local_authority']])