import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from glob import glob
import os


def app():

    col1, col2 = st.columns(2)
    
    with col1:
        st.header('Correlation Matrix')

    with col2:
        uploaded_file = st.file_uploader("Uplaod .csv file", type = ['.csv'])
        if uploaded_file is not None:
            [os.remove(file) for file in glob('csv_file/*')]
            with open(os.path.join("csv_file", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())

    df = pd.read_csv(glob('csv_file/*')[0])

    cols = [x for x in df.columns if df[x].dtype != 'O']
    cols.insert(0, 'All columns')

    col1, col2 = st.columns(2)

    with col1:
        columns = st.multiselect('Select Columns', cols, ['All columns'])

    with col2:
        cmap = st.selectbox('Style', ['Viridis', 'Plasma', 'Inferno', 'Magma', 'Cividis'])

    if st.button('Plot'):

        fig = plt.figure(figsize=(12, 8))
        sns.set_style('darkgrid')

        if columns[0] == 'All columns' and len(columns) == 1:
            sns.heatmap(df.corr(), annot = True, cmap = cmap.lower())
        else:
            if 'All columns' in columns:
                sns.heatmap(df.corr(), annot = True, cmap = cmap.lower())
            else:
                sns.heatmap(df[columns].corr(), annot = True, cmap = cmap.lower())

        st.pyplot(fig)
