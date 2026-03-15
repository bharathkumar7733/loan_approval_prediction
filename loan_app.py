import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("loan_model.pkl","rb"))

st.title("Loan Approval Prediction")

income = st.number_input("Income")
credit_score = st.number_input("Credit Score")
loan_amount = st.number_input("Loan Amount")
employment = st.selectbox("Employment Status",[0,1])

if st.button("Predict Loan"):

    input_data = pd.DataFrame({
        "income":[income],
        "credit_score":[credit_score],
        "loan_amount":[loan_amount],
        "employment_status":[employment]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")