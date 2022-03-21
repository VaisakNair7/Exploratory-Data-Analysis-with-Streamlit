import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from glob import glob
import os

def app():

    col1, col2 = st.columns(2)
    
    with col1:
        st.header('Box Plot')

    with col2:
        uploaded_file = st.file_uploader("Uplaod .csv file", type = ['.csv'])
        if uploaded_file is not None:
            [os.remove(file) for file in glob('csv_file/*')]
            with open(os.path.join("csv_file", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())

    df = pd.read_csv(glob('csv_file/*')[0])

    cols = df.columns
    final_cols = cols.insert(0, None)

    num_cols = [x for x in df.columns if df[x].dtype != 'O']
    num_cols.insert(0, None)

    palettes = ['Bright', 'Dark', 'Deep', 'Muted', 'Pastel', 'Colorblind']

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        x = st.selectbox('Select X axis', final_cols)

    with col2:
        y = st.selectbox('Select Y axis', final_cols)

    with col3:
        hue = st.selectbox('Select Hue column', final_cols, index = 0)

    with col4:
        orient = st.selectbox('Orientation', ['Vertical', 'Horizontal'])

    with col5:
        palette = st.selectbox('Select Style', palettes)

    if st.button('Plot'):   

        fig = plt.figure(figsize=(12, 6)) 
        sns.set_style('darkgrid')
        
        if x is None and y is not None:
            try:
                sns.boxplot(data = df, y = y, hue = hue, palette = palette.lower())
            except Exception as e:
                st.error(e)
        if x is not None and y is None:
            try:
                sns.boxplot(data = df, x = x, hue = hue, palette = palette.lower())
            except Exception as e:
                st.error(e)
        if x is not None and y is not None:
            if orient == 'Vertical':
                try:
                    sns.boxplot(data = df, x = x, y = y, hue = hue, palette = palette.lower(), orient = 'v') 
                except Exception as e:
                    st.error(e)
            else:
                try:
                    sns.boxplot(data = df, x = x, y = y, hue = hue, palette = palette.lower(), orient = 'h')
                except Exception as e:
                    st.error(e)
                  
        st.pyplot(fig)