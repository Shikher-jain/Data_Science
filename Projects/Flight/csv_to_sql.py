import os
import csv
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MySQL
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT", 3306))
)

cursor = conn.cursor()

# Optional: create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS flights (
    Airline VARCHAR(100),
    Date_of_Journey DATE,
    Source VARCHAR(50),
    Destination VARCHAR(50),
    Route VARCHAR(200),
    Dep_Time TIME,
    Duration VARCHAR(50),
    Total_Stops INT,
    Price FLOAT
)
""")
conn.commit()

# Open CSV and insert row by row
with open("flights_cleaned.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO flights 
            (Airline, Date_of_Journey, Source, Destination, Route, Dep_Time, Duration, Total_Stops, Price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["Airline"],
            row["Date_of_Journey"],
            row["Source"],
            row["Destination"],
            row["Route"],
            row["Dep_Time"],
            row["Duration"],
            int(row["Total_Stops"]) if row["Total_Stops"] else 0,
            float(row["Price"]) if row["Price"] else 0.0
        ))
    conn.commit()

print("CSV data manually loaded successfully using .env credentials!")

cursor.close()
conn.close()
