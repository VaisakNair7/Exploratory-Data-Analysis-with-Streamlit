import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from glob import glob
import os

def app():

    col1, col2 = st.columns(2)
    
    with col1:
        st.header('Count Plot')

    with col2:
        uploaded_file = st.file_uploader("Uplaod .csv file", type = ['.csv'])
        if uploaded_file is not None:
            [os.remove(file) for file in glob('csv_file/*')]
            with open(os.path.join("csv_file", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())

    df = pd.read_csv(glob('csv_file/*')[0])

    cols = df.columns
    final_cols = cols.insert(0, None)

    palettes = ['Bright', 'Dark', 'Deep', 'Muted', 'Pastel', 'Colorblind']

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        c = st.selectbox('Select Column', cols)

    with col2:
        orient = st.selectbox('Select Oreintation', ['Vertical', 'Horizontal'])

    with col3:
        hue = st.selectbox('Select Hue column', final_cols, index = 0)

    with col4:
        palette = st.selectbox('Select Style', palettes)

    if st.button('Plot'):    
        sns.set_style('darkgrid')
        
        if orient == 'Vertical':
            fig = plt.figure(figsize=(12, 6))
            sns.countplot(data = df, x = c, hue = hue, palette = palette.lower())
            plt.xticks(rotation = 45)
        else:
            fig = plt.figure(figsize=(8, 6))
            sns.countplot(data = df, y = c, hue = hue, palette = palette.lower())
            plt.yticks(rotation = 45)
            
        st.pyplot(fig)