from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

host = "localhost"
user = "root"
password = quote_plus("sh!kherj@!n786")
database = "practice"

engine = create_engine(
    f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM order_items"))
    for row in result:
        print(row)
connection.close()

# PostgreSQL 

# engine = create_engine(
#     "postgresql+psycopg2://postgres:password@localhost:5432/practice"
# )

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM order_items"))
#     for row in result:
#         print(row)