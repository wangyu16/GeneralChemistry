import streamlit as st
from sigfig import round
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import requests
copyright = requests.get("https://raw.githubusercontent.com/wangyu16/PolymerScienceEducation/master/copyright.md")

r1 = st.number_input('r1',min_value=0)
r2 = st.number_input('r2',min_value=0)
f1_0 = st.slider('f1_0',min_value = 0, max_value = 1, step = 0.01)

Nt_0=1000000 # Set the total number of monomers. 

# Define a function to determine which monomer to add.
def add_monomer(r1,r2,f1,chainend):
  if chainend == 1:
    chance_1 = r1*f1/(r1*f1-f1+1)
  else:
    chance_1 = f1/(f1+r2-r2*f1)
  #print(chance_1)
  if np.random.random() < chance_1:
    return 1
  else:
    return 2

# Randomize the initial monomer unit simply based on the monomer fraction. 
if np.random.random()<f1_0:
  M0 = 1
else:
  M0 = 2

# Create an object to store the polymer chain sequence, 
# monomer 1 fraction in the feedstock,
# fraction of monomer 1 incoporating into the polymer at this moment,
# cumulative monomer 1 fraction in the polymer.
chains = [[M0],[f1_0],[0],[0]]

N1_0=Nt_0*f1_0
Nt=Nt_0
N1=N1_0
f1=f1_0

# Construct the polymer chain.
for i in range(Nt):
  monomer = add_monomer(r1,r2,f1,chains[0][-1])
  Nt-=1
  if monomer == 1:
    N1-=1
  if Nt > 0:
    f1 = N1/Nt
  else:
    f1 = 0
  F1= (r1*f1**2+f1*(1-f1))/(r1*f1**2+2*f1*(1-f1)+r2*(1-f1)**2)
  
  if Nt_0==Nt:
    F_cumu = 0
  else:
    F_cumu = (N1_0-N1)/(Nt_0-Nt)

  chains[0].append(monomer)
  chains[1].append(f1)
  chains[2].append(F1)
  chains[3].append(F_cumu)

# Select the information to be reported

chain_secs = np.empty(shape=(99,100))
info = {'Overall monomer conversion':[],'Feedstock fraction of 1':[],'Cumulative fraction of 1 in polymers':[],'Fraction of 1 incoporating into polymers':[],'Fraction of 1 in sample chain section':[]}
df_info = pd.DataFrame(info)

for i in range(1,100):
  sta=int(abs(i*Nt_0/100))
  chain_secs[i-1]=chains[0][sta-50:sta+50]
  df_info.loc[len(df_info.index)] = [sta/Nt_0*100,chains[1][sta]*100,chains[3][sta]*100,chains[2][sta]*100,chains[0][sta-50:sta+50].count(1)] 

fig = plt.figure()
plt.rcParams["figure.figsize"] = (7.5,7.5)
f1 = np.linspace(0,1, 100)
F1= (r1*f1**2+f1*(1-f1))/(r1*f1**2+2*f1*(1-f1)+r2*(1-f1)**2)
plt.plot(f1,f1,'k--',linewidth=0.5)
plt.plot(f1,F1)
plt.xlabel('f1')
plt.ylabel('F1')
st.pyplot(fig)

st.markdown("### Copyright")
st.write(copyright.text)
