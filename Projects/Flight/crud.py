import mysql.connector

from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME'),
        port = os.getenv('DB_PORT', 3306),
        allow_local_infile=True,
        use_pure=True

        )
    mycursor = conn.cursor()
    if conn.is_connected():
        # db_info = conn.get_server_info()
        print(f"Successfully connected to MySQL Server ")
except:
    print(f"Failed to connect to MySQL Server")

# mycursor.execute("CREATE DATABASE IF NOT EXISTS flight_database")
# conn.commit()

# mycursor.execute("USE flight_database")
# conn.commit()

# mycursor.execute("CREATE TABLE IF NOT EXISTS flights (id INT AUTO_INCREMENT PRIMARY KEY, airline VARCHAR(255), date_of_journey DATE, source VARCHAR(255), destination VARCHAR(255), route VARCHAR(255), dep_time TIME, duration VARCHAR(50), total_stops INT, price FLOAT)")
# conn.commit()

# mycursor.execute("""
#                  INSERT INTO flights
#                  (airline, date_of_journey, source, destination, route, dep_time, duration, total_stops, price) VALUES 
#                  ('IndiGo', '2023-10-15', 'Delhi', 'Mumbai', 'DEL-MUM', '10:00:00', '2h 30m', 0, 4500.00)
#                  """)
# conn.commit()

# mycursor.execute("SELECT * FROM flights")
# for row in mycursor.fetchall():
#     print(row)
#     print(row[-1])

# mycursor.execute("UPDATE flights SET price = price + 500 WHERE airline = 'IndiGo'")


# mycursor.execute("SELECT * FROM flights WHERE airline = \"Indigo\"")
# for row in mycursor.fetchall():
#     print(row)
#     print(row[-1])

# mycursor.execute("DELETE FROM flights WHERE airline = 'IndiGo'")
# conn.commit()

# mycursor.execute("SELECT * FROM flights WHERE airline = \"Indigo\"")
# for row in mycursor.fetchall():
#     print(row)

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}",    pool_pre_ping=True,
)

for chunk in pd.read_csv("flights_cleaned.csv", chunksize=5000):
    chunk.to_sql("flights", engine, if_exists="append", index=False)

print("CSV data loaded successfully.")