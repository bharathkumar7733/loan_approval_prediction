import pickle
import pandas as pd

# load model
model = pickle.load(open("loan_model.pkl","rb"))

print("Loan Approval Prediction System")

income = int(input("Enter yearly income: "))
credit_score = int(input("Enter credit score: "))
loan_amount = int(input("Enter loan amount: "))
employment = int(input("Employment status (1 = employed, 0 = unemployed): "))

# create dataframe with feature names
input_data = pd.DataFrame({
"income":[income],
"credit_score":[credit_score],
"loan_amount":[loan_amount],
"employment_status":[employment]
})

prediction = model.predict(input_data)

print("\nPrediction Result:")

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")