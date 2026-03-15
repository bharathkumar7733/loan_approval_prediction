# Loan Approval Prediction System
^ 📌 Project Overview ^

The **Loan Approval Prediction System** is a Machine Learning project that predicts whether a loan application will be **approved or rejected** based on financial and employment data.

The system uses a trained **Decision Tree Machine Learning model** to analyze user inputs and make predictions.

This project demonstrates:

* Machine Learning model training
* SQL database integration
* Data preprocessing
* AI prediction
* Simple user interface for predictions

------

## 🧠 Technologies Used

* Python
* SQLite Database
* scikit-learn (Machine Learning)
* Pandas
* Streamlit (for UI)

---

## 📂 Project Structure

```
loan-approval-project
│
├── database_setup.py      # Creates database and inserts sample data
├── train_model.py         # Trains machine learning model
├── predict.py             # Predicts loan approval from user input
├── loan_model.pkl         # Saved trained ML model
├── loan.db                # SQLite database
├── loan_app.py            # Streamlit UI
└── README.md
```

---

## ⚙️ How the System Works

1. **Database Creation**

   * Loan applicant data is stored in a SQLite database.

2. **Data Processing**

   * Data is extracted and converted into features.

3. **Model Training**

   * A Decision Tree Classifier is trained using historical loan data.

4. **Prediction**

   * User inputs financial information.
   * The ML model predicts loan approval.

5. **User Interface**

   * A simple Streamlit UI allows users to enter inputs and get predictions.

---

## 🚀 Installation and Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/loan-approval-prediction.git
cd loan-approval-prediction
```

### 2️⃣ Install Dependencies

```
pip install pandas scikit-learn streamlit
```

### 3️⃣ Create the Database

```
python database_setup.py
```

### 4️⃣ Train the Model

```
python train_model.py
```

### 5️⃣ Run the Prediction System

```
python predict.py
```

---

## 🌐 Run the Web UI

To launch the web interface:

```
streamlit run loan_app.py
```

Your browser will open automatically.

---

## 📊 Input Features Used

The model uses the following features:

* Income
* Credit Score
* Loan Amount
* Employment Status

---

## 🎯 Example Prediction

Input:

```
Income: 60000
Credit Score: 720
Loan Amount: 200000
Employment: Employed
```

Output:

```
Loan Approved
```

---

## 📈 Future Improvements

Possible upgrades for the project:

* Loan approval probability score
* Risk classification (Low / Medium / High)
* Data visualization dashboard
* AI explanation for predictions
* Deployment on cloud platforms

---

## 💼 Resume Value

This project demonstrates:

✔ Machine Learning model development
✔ Database integration with SQL
✔ Data preprocessing and feature engineering
✔ AI-based prediction system
✔ Web interface for ML models

---

## 👨‍💻 Author

**Bharath Kumar**

Computer Science Student
Interested in AI, Machine Learning, and Software Development

---
