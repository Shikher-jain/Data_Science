import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("create table if not exists order_items (id integer primary key, name text, quantity integer)")
cursor.execute("""insert into order_items (name, quantity) values 
                    ('item1', 10),
                    ('item2', 10),
                    ('item3', 10),
                    ('item4', 10),
                    ('item5', 10),
                    ('item6', 10),
                    ('item7', 10),
                    ('item8', 10),
                    ('item9', 10),
                    ('item10', 10),
                    ('item11', 10),
                    ('item12', 10),
                    ('item13', 10),
                    ('item14', 10),
                    ('item15', 10),
                    ('item16', 10),
                    ('item17', 10),
                    ('item18', 10),
                    ('item19', 10),
                    ('item20', 10)
               """)

cursor.execute("SELECT * FROM order_items")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()