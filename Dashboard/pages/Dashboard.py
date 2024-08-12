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
min_age, max_age = st.sidebar.slider('Age',
                        min_value = int(titanic['age'].min()),
                        max_value = int(titanic['age'].max()),
                        value = (int(titanic['age'].min()), int(titanic['age'].max())))
# Filter the dataset based on selections
filtered_data = titanic[
    (titanic['sex'].isin(gender)) &
    (titanic['pclass'].isin(pclass)) &
    (titanic['age'] >= min_age) & 
    (titanic['age'] <= max_age)
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

#Scatter plot of age vs fare
st.subheader("Age vs. Fare")
fig = px.scatter(filtered_data, x='age', y='fare', color='survived', title="Age vs. Fare",
                 labels = {'age':'Age','fare':'Fare'})
st.plotly_chart(fig)

#Box plot of age distribution by passenger class
st.subheader('Age Distribution by Class')
fig = px.box(filtered_data, x='pclass', y='age', title="Age Distribution by Class", labels={'pclass' : 'Class','age':'Age'})
st.plotly_chart(fig)

# Create a bar chart of survival counts
st.subheader('Survival Counts')
survival_count = filtered_data['survived'].value_counts().reset_index()
survival_count.columns=['survived','count']
fig = px.bar(survival_count, x='count',y='survived', orientation='h', title='Survival Counts',
             labels = {'survived' : 'Survived', 'count' : 'Count'},text='count')
st.plotly_chart(fig)

# Passenger class counts
st.subheader('Passenger Class Counts')
class_Counts = filtered_data['pclass'].value_counts().reset_index()
class_Counts.columns = ['pclass', 'count']
fig = px.pie(class_Counts, values='count', names='pclass', hole=0.4, title = 'Passesnger Class Counts' )
st.plotly_chart(fig)

# Bar chart of fare distribution by passenger class
st.subheader('Fare Distribution by Class')
fig = px.bar(filtered_data, x = 'pclass', y= 'fare', title = 'Fare Distribution by Class',
             labels = {'pclass' : 'Passengers Class', 'fare' : 'Fare'}, barmode = 'group')
st.plotly_chart(fig)

# KDE Plot of age distribution by survival status
st.subheader('Age Distribution by Survival Status')
fig = px.density_contour(filtered_data, x='age', color='survived', title='Age Distribution by Survival Status',
                         labels={'age':'Age', 'density':'Density'})
st.plotly_chart(fig)
