import imaplib
import imp
import re
from string import printable
from xml.dom.minidom import Element
import psycopg2
from scemas import SensorData, SensorOneData, SensorTwoData, SensorThreeData
from psycopg2.extras import RealDictCursor

class Postgres:
    # Connect to an existing database
    HOST = '127.0.0.1'
    PORT = 5432
    USER = 'postgres'
    PASS = '51555'
    NAME = 'SmartDB'
    
    def __init__(self):
        self.DATABASE_URL = f'postgresql://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}'

    def __enter__(self):
        self.conn = psycopg2.connect(self.DATABASE_URL,cursor_factory=RealDictCursor)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.cur.close()

def get_last_three_value():
    with Postgres() as cur:
        cur.execute('SELECT * FROM "SensorsData" ORDER BY "Time" limit 3')
        return [SensorData(**elemnt) for elemnt in cur.fetchall()]

def get_sensor_one_data(limit = 3):
    with Postgres() as cur:
        cur.execute('SELECT "D1","Time" FROM "SensorsData" ORDER BY "Time" limit '+limit)
        return [SensorOneData(**elemnt) for elemnt in cur.fetchall()]

def get_sensor_two_data():
    with Postgres() as cur:
        cur.execute('SELECT "D2","Time" FROM "SensorsData" ORDER BY "Time" limit 3')
        return [SensorTwoData(**elemnt) for elemnt in cur.fetchall()]

def get_sensor_three_data():
    with Postgres() as cur:
        cur.execute('SELECT "D3","Time" FROM "SensorsData" ORDER BY "Time" limit 3')
        return [SensorThreeData(**elemnt) for elemnt in cur.fetchall()]