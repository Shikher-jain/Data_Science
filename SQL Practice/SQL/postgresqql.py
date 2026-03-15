import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="portfolio_db",
    user="your_username",
    password="your_password"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM contact_form")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()

