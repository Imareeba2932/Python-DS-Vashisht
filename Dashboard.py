import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Set the title of the dashboard
st.title("Titanic Dataset Dashboard")

st.sidebar.header('Filter Options')

# Gender Filter
gender = st.sidebar.multiselect('Gender',
                                options = titanic['sex'].unique(),
                                default = titanic['sex'].unique())

# Class Filter
pclass = st.sidebar.multiselect('Class',
                                options = sorted(titanic['pclass'].unique()),
                                 default = sorted(titanic['pclass'].unique()))

# Age Filter
age = st.sidebar.slider('Age',
                        min_value = int(titanic['age'].min()),
                        max_value = int(titanic['age'].max()),
                        value = (int(titanic['age'].min()), int(titanic['age'].max())))

# Filter the dataset based on selections
filtered_data = titanic[
    (titanic['sex'].isin(gender)) &
    (titanic['pclass'].isin(pclass)) &
    (titanic['age'] >= age[0] & (titanic['age'] <= age[1]))
]

st.dataframe(filtered_data)


#Create a pie chart of gender distribution
st.subheader('Gender Distribution')
gender_count = filtered_data['sex'].value_counts()
fig = px.pie(names=gender_count.index, values = gender_count.values, title = "Gender Distribution")
st.plotly_chart(fig)

#Create a histogram of age distribution
st.subheader('Age Distribution')
fig = px.histogram(filtered_data, x='age', nbins=30, title='Age Distribution',
                    labels={'age':'Age','count':'Frequency'},marginal='box')
st.plotly_chart(fig)

#Violin plot of age distribution by survival status
st.subheader('Age Distribution by Survival Status')
fig = px.violin(filtered_data, x='survived',y='age', title='Age Distribution by Survival Status',
                labels={'survived':'Survived','age':'Age'},box=True, points='all')
st.plotly_chart(fig)