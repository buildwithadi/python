import streamlit as st
import numpy as np
import pandas as pd

st.title("StreamLit Text Input")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:",0,100,25)

options = ["Python", "Dart", "Java", "C++"]
choice = st.selectbox("Choose your favorite language:",options)

upload_file = st.file_uploader("Choose a CSV file", type="csv")
df = pd.read_csv(upload_file)

if upload_file is not None:
    st.write(df)

if name:
    st.write(f"Hello, {name}👋")

st.write(f"Your age is {age}")
st.write(f"Your favourite language is {choice}")


chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)