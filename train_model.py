import sqlite3
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# connect to SQL database
conn = sqlite3.connect("loan.db")

# read table into dataframe
query = "SELECT * FROM loan_data"
data = pd.read_sql_query(query, conn)

print("Dataset Loaded:")
print(data)

# separate features and target
X = data[['income','credit_score','loan_amount','employment_status']]
y = data['loan_status']

# split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining data prepared")

# create machine learning model
model = DecisionTreeClassifier()

# train the model
model.fit(X_train, y_train)

print("\nModel training completed")

# test model accuracy
accuracy = model.score(X_test, y_test)

print("\nModel Accuracy:", accuracy)

# save trained model
pickle.dump(model, open("loan_model.pkl","wb"))

print("\nModel saved as loan_model.pkl")

conn.close()