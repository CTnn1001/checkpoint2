import pandas as pd
import streamlit as st 

st.title("Hello, my first app") 
st.write("Day la ung dung dau tien cua toi")

df = pd.read_csv("lettuce_dataset.csv") 
st.line_chare(df)
