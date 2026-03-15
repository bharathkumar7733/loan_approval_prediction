import sqlite3

# connect to database (creates loan.db if not present)
conn = sqlite3.connect("loan.db")

cursor = conn.cursor()

# create loan table
cursor.execute("""
CREATE TABLE IF NOT EXISTS loan_data(
income INTEGER,
credit_score INTEGER,
loan_amount INTEGER,
employment_status INTEGER,
loan_status INTEGER
)
""")

# sample training data
data = [
(50000,700,200000,1,1),
(30000,650,150000,1,1),
(20000,500,100000,0,0),
(80000,750,300000,1,1),
(25000,480,120000,0,0),
(60000,720,250000,1,1),
(22000,510,90000,0,0),
(45000,680,180000,1,1),
(27000,520,110000,0,0),
(72000,740,260000,1,1)
]

# insert data
cursor.executemany("INSERT INTO loan_data VALUES (?,?,?,?,?)", data)

conn.commit()

print("Database created and data inserted successfully")

conn.close()