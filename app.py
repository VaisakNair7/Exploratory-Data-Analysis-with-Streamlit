import streamlit as st
from glob import glob
from multiapp import MultiApp
from apps import line, bar, count, scatter, box, hist, kde, violin, qq, corr

st.set_page_config(
    page_title = "Exploratory Data Analysis",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

st.title("""
    Exploratory Data Analysis
    """)

with st.sidebar.expander('Contact'):
    st.write('[GitHub](https://github.com/VaisakNair7/Exploratory-Data-Analysis-with-Streamlit)')
    st.write('[LinkedIn](https://www.linkedin.com/in/vaisaksnair/)')
    st.write('Mail : vaisaksnair98@gmail.com')

st.sidebar.write(' ')

app = MultiApp()
app.add_app("Line Plot", line.app)
app.add_app("Bar Plot", bar.app)
app.add_app("Count Plot", count.app)
app.add_app("Scatter Plot", scatter.app)
app.add_app("Box Plot", box.app)
app.add_app("Histogram", hist.app)
app.add_app("Density Plot", kde.app)
app.add_app("Violin Plot", violin.app)
app.add_app("Q-Q Plot", qq.app)
app.add_app("Correlation Matrix", corr.app)
app.run()
