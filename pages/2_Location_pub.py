import streamlit as st
import numpy as np
import pandas as pd

st.header("Pubs with respect to location")


# loading the data
df = pd.read_csv(r"C:\Users\bhask\Desktop\DATA SCIENCE AND ANALYTICS\Internship_Inno\FLASK\Pub_Nearest_project\resources\open_pubs_cleaned.csv")

single = ['All','Post Code', 'Local authority', 'Pub name']

selection = st.selectbox( label = "Select the option for pubs available", options = single, )

if selection=='Post Code':
    selected=st.selectbox(label='Select the ZipCode',options=df['postcode'].unique())
    st.subheader(f"Total Pubs Found : {df[df['postcode']==selected].shape[0]}")
    st.map(data=df[df['postcode']==selected],  use_container_width=True)
elif selection=='Local Authority':
    selected=st.selectbox(label='Select Local Authority',options=df['local_authority'].unique())
    st.subheader(f"Total Pubs Found : {df[df['local_authority']==selected].shape[0]}")
    st.map(data=df[df['local_authority']==selected],  use_container_width=True)
elif selection=='Pub Name':
    selected=st.selectbox(label='Select the Pub Name',options=df['name'].unique())
    st.subheader(f"Total Pubs Found : {df[df['name']==selected].shape[0]}")
    st.map(data=df[df['name']==selected],  use_container_width=True)    
else:
    st.subheader(f"Total Pubs Found : {df.shape[0]}")
    st.map(data=df,  use_container_width=True)