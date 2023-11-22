import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'


st.title('Build and shared data application!')

with st.container():
    st.write("This is inside the first container")

    df_cars = pd.read_csv(url)

    option = st.selectbox(
    'Select a Continent',
    df_cars['continent'].unique())

st.write("This is outside the container")

fig, ax = plt.subplots()
sns.heatmap(df_cars[df_cars['continent'] == option].drop(columns='continent').corr(),
            annot=True, 
            cmap='coolwarm')

ax.set(xlabel='Titre')

st.write(fig)

st.write('You selected:', option)

fig, ax = plt.subplots()
sns.histplot(data=df_cars[df_cars['continent'] == option], x='hp')

ax.set(xlabel='Titre')

st.write(fig)
