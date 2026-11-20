import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_model.pkl")

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

st.title("🏠 House Price Prediction")
st.write("Enter house details to predict the price.")

area = st.number_input("Area (Square Feet)", min_value=1, value=1500)
bedroom = st.number_input("Bedrooms", min_value=1, value=3)
bathroom = st.number_input("Bathrooms", min_value=1, value=2)
age = st.number_input("House Age", min_value=0, value=5)

if st.button("Predict House Price"):

    input_data = pd.DataFrame(
        [[area, bedroom, bathroom, age]],
        columns=["Area", "Bedroom", "Bathroom", "Age"]
    )

    prediction = model.predict(input_data)[0]

    st.success("Prediction Completed!")
    st.metric("Estimated House Price", f"₹ {prediction:,.2f}")