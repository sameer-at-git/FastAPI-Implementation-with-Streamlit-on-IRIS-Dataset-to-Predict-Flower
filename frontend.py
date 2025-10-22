import streamlit as st
import httpx
from constants import ASSETS_PATH

url ="https://fastapi-implementation-with-streamlit-on.onrender.com/docs#/default/predict_flower_api_iris_v1_predict_post"

def predict_flower(payload):
    with httpx.Client(timeout=10) as client:
        response = client.post(url, json=payload)
        response.raise_for_status()
        return response


st.markdown("# Iris Flower Prediction App")

with st.form("iris_form"):
    sepal_length=st.number_input("Sepal Length(cm)", min_value=4.01, max_value=8.49, value=6.0)
    sepal_width=st.number_input("Sepal Width(cm)", min_value=1.81, max_value=4.99, value=2.5)
    petal_length=st.number_input("Petal Length(cm)", min_value=0.81, max_value=7.49, value=4.5)
    petal_width=st.number_input("Petal Width(cm)", min_value=0.01, max_value=2.99, value=1.2)

    submitted = st.form_submit_button("Predict Flower")

if submitted:
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    with st.spinner("Predicting..."):
        response = predict_flower(payload=payload)
    st.success("Prediction Complete!")
    result = response.json()
    flower = result['predicted_flower']
    st.markdown(f"## Predicted Flower: {flower}")
    flower_image_path = ASSETS_PATH / f"{flower}.jpg"
    st.image(flower_image_path, caption=flower, use_column_width=True)