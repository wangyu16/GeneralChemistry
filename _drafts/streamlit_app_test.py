import streamlit as st
import pandas as pd
from sigfig import round
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import requests
copyright = requests.get("https://raw.githubusercontent.com/wangyu16/PolymerScienceEducation/master/copyright.md")


st.title("Test")
st.write(f"Round 3.1415926 in 3 significant figure gives {round(3.1415926,3)}")
x = st.slider('Select a value',min_value=0, max_value=5)
df = pd.DataFrame({
  'first column': [-4,-3,-2,-1,0,1, 2, 3, 4],
  'second column': [(-4)**x,(-3)**x,(-2)**x,(-1)**x,0**x,1**x, 2**x, 3**x, 4**x]
})

fig = plt.figure()
plt.plot(df['first column'],df['second column'])
st.pyplot(fig)


st.write(x, 'squared is', x * x)
st.markdown("### Copyright")
st.write(copyright.text)
