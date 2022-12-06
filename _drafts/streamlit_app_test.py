import streamlit as st
import pandas as pd
from sigfig import round

st.title("Test")
st.write(f"Round 3.1415926 in 3 significant figure gives {round(3.1415926,3)}")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
