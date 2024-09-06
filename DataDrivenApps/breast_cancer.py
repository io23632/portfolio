import pandas as pd
import streamlit as st
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


st.write("""
         # Breast Cancer Prediction App
         This app uses Machine Learning and the mean tumor size radius to for breast cancer tumor classification
         
         """)

br_data = load_breast_cancer()
data_df = pd.DataFrame(data=br_data.data, columns=br_data.feature_names)

# Extract the mean radius feature :
mean_radii_df = data_df[['mean radius']] # The double brackets keep the data as a df
# Extract the target :
target_df = pd.DataFrame(data=br_data.target, columns=['target'])
# Concat to one data frame:
df = pd.concat([mean_radii_df, target_df], axis=1)

# Produce testing set: 
X = df[['mean radius']] # The double brackets keep the data as a df
Y = df[['target']]
# Split the data set into testing and training here I am doing a train/test of 80/20
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = RandomForestClassifier(random_state=42) 
model.fit(X_train, Y_train)

mean_radius = st.slider('Mean radius:', 6.0, 30.0, 11.0)

prediction = model.predict([[mean_radius]])

prediction_label = 'Benign' if prediction[0] == 1 else 'Malignant'

st.write(f'The tumor based on your mean radius size of {mean_radius} The tumor is {prediction_label}')

model_accuracy = accuracy_score(Y_test, model.predict(X_test))

st.write(f'The accuracy of the model being used is: {model_accuracy * 100: .2f}%')
