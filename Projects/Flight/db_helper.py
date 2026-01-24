import mysql.connector

from dotenv import load_dotenv
import os

load_dotenv()
class DB():

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = os.getenv('DB_HOST'),
                user = os.getenv('DB_USER'),
                password = os.getenv('DB_PASSWORD'),
                database = os.getenv('DB_NAME'),
                port = os.getenv('DB_PORT', 3306),
                allow_local_infile=True,
                use_pure=True

                )
            self.mycursor = self.conn.cursor()
            if self.conn.is_connected():
                # db_info = conn.get_server_info()
                print(f"Successfully connected to MySQL Server ")
        except:
            print(f"Failed to connect to MySQL Server")

    def fetch_city_names(self):
        self.mycursor.execute("SELECT DISTINCT source FROM flights UNION SELECT DISTINCT destination FROM flights")
        cities = [row[0] for row in self.mycursor.fetchall()]
        # cities = self.mycursor.fetchall()
        # print(cities) 
        cities.sort()
        return cities
        
    def fetch_destination_city_names(self):
        self.mycursor.execute("SELECT DISTINCT destination FROM flights")
        cities = [row[0] for row in self.mycursor.fetchall()]
        # cities = self.mycursor.fetchall()
        # print(cities) 
        cities.sort()
        return cities

    def fetch_source_city_names(self):
        self.mycursor.execute("SELECT DISTINCT source FROM flights")
        cities = [row[0] for row in self.mycursor.fetchall()]
        # cities = self.mycursor.fetchall()
        # print(cities) 
        cities.sort()
        return cities
    
    def fetch_all_flights (self,source, destination):
        self.mycursor.execute("SELECT * FROM flights Where source=%s AND destination=%s",(source,destination)     )
        data = self.mycursor.fetchall()
        return data
    
    def fetch_airline_frequencies(self):
        self.mycursor.execute("select airline ,count(*) from flights group by airline")
        data = self.mycursor.fetchall()

        airline = [row[0] for row in data]        
        freqency = [row[1] for row in data]
        
        return airline , freqency

    def fetch_busy_airport(self):
        self.mycursor.execute("SELECT source, count(*) FROM (SELECT source FROM flights union all SELECT destination FROM flights) t group by t.source order by count(*) desc")
        data = self.mycursor.fetchall()
    
        return data
        
    def daily_freq(self):
        self.mycursor.execute("SELECT Date_of_Journey, count(*) FROM flights group by Date_of_Journey")
        data = self.mycursor.fetchall()

        return data