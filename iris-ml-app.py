import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# meor-my first application
# Simple Iris Flower Prediction App

This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

st.image("https://www.gardendesign.com/pictures/images/900x705Max/site_3/iris-louisiana-black-gamecock-iris-beardless-louisiana-iris-shutterstock-com_12592.jpg", caption='Credit to GardenDesign')

st.image("https://www.google.com.my/search?q=iris+flower+jpg&hl=en&tbm=isch&sxsrf=ALiCzsZgk9JgySITvVNPbBHwKmoAVSFI4w%3A1661324747138&source=hp&biw=1366&bih=657&ei=y80FY7TGBpPAhwPB7aDYCA&iflsig=AJiK0e8AAAAAYwXb21ijRxrNIade0nKlk3iklHP3p-JJ&oq=iris+&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgQIIxAnMgsIABCABBCxAxCDATIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CAgAELEDEIMBUNoGWPINYMMaaABwAHgBgAH2B4gB6wqSAQU1LjctMZgBAKABAaoBC2d3cy13aXotaW1nsAEA&sclient=img#imgrc=vCpw_dM_NYAraM")
