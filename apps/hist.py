import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from glob import glob
import os

def app():

    col1, col2 = st.columns(2)
    
    with col1:
        st.header('Histogram')

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
        c = st.selectbox('Select column', cols)

    with col2:
        hue = st.selectbox('Select Hue column', final_cols, index = 0)

    with col3:
        bins = st.number_input('Select no of bins', step = 1, min_value = 1, value = 30)

    with col4:
        palette = st.selectbox('Select Style', palettes)

    if st.button('Plot'):    
        
        fig = plt.figure(figsize = (12, 6))
        sns.set_style('darkgrid')
        try:    
            sns.histplot(data = df, x = c, bins = bins, hue = hue, palette = palette.lower())
            st.pyplot(fig)
        except:
            st.write('Error! Please check for missing values in the dataset.')