import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

# Title:
st.write("""
         # Iris Flow Predictor
         
         This web app uses Classification model to classify the **iris flower types** based on the 
         input parameters in the sidebar
         
         """)

# Side Bar: 

st.sidebar.header('Input Parameters')

def define_parameters():
    # Create Sidebar parameters: 
    sepal_lenght = st.sidebar.slider('Sepal Lenght', 4.3, 7.9, 5.0)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.0)
    petal_length = st.sidebar.slider('Petal Lenght', 1.0, 6.9, 1.5)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 1.0)
    #Create the data dictionary: 
    data = {
        'sepal_length': sepal_lenght,
        'sepal_width': sepal_width,
        'petal_lenght': petal_length,
        'petal_width' : petal_width
    }
    # Convert into pandas dataframe: 
    featuers = pd.DataFrame(data, index=[0])
    return featuers

df = define_parameters()
st.write(df)


# Retrieve the iris dataset set from the datasets module:
iris = datasets.load_iris()
# Import the data set featuers and targets
X = iris.data
Y = iris.target

# Use the randomforest classifier to fit the dataset
clf = RandomForestClassifier()
clf.fit(X, Y)

#make the prediciton
prediction = clf.predict(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])