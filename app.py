import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Sales Prediction App")

youtube = st.number_input("YouTube ad budget", min_value=0.0)
facebook = st.number_input("Facebook ad budget", min_value=0.0)
newspaper = st.number_input("Newspaper ad budget", min_value=0.0)

if st.button("Predict"):
    result = model.predict([[youtube, facebook, newspaper]])
    st.success(f"Predicted sales: {result[0]:.2f}")
