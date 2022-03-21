import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import probplot
from glob import glob
import os

def app():

    col1, col2 = st.columns(2)
    
    with col1:
        st.header('Q-Q Plot')

    with col2:
        uploaded_file = st.file_uploader("Uplaod .csv file", type = ['.csv'])
        if uploaded_file is not None:
            [os.remove(file) for file in glob('csv_file/*')]
            with open(os.path.join("csv_file", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())

    df = pd.read_csv(glob('csv_file/*')[0])

    c = st.selectbox('Select column', [x for x in df.columns if df[x].dtype != 'O'])

    if st.button('Plot'):    
        
        sns.set_style('darkgrid')
        fig = plt.figure(figsize = (12, 6))
        probplot(x = df[c], plot = plt)
        st.pyplot(fig)