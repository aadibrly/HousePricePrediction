import streamlit as st
import pickle
import numpy as np

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("House Price Estimator")
st.write("Predict home values using real machine learning model trained on housing metrics.")

rooms = st.slider("Average Number of Rooms (RM)", 3.0, 9.0, 6.0, step=0.1)
lstat = st.slider("Neighborhood Socioeconomic Level (% LSTAT)", 1.0, 40.0, 12.0, step=0.5)
ptratio = st.slider("Pupil-Teacher Ratio (PTRATIO)", 12.0, 22.0, 18.0, step=0.5)

if st.button("Calculate Estimated Price"):
    features = np.array([[rooms, lstat, ptratio]])
    prediction = model.predict(features)[0]
    st.success(f"Estimated Price: ${prediction * 1000:,.2f}")

