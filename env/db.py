# from sqlalchemy import create_engine, MetaData

# engine = create_engine('mysql+pymysql://root@localhost:3306/du_an_ban_dat')
# meta=MetaData()
# con= engine.connect()

import mysql.connector
from dotenv import load_dotenv
import json
import datetime
from json import JSONEncoder
import bson
# Load environment variables
load_dotenv()

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Password12@"
MYSQL_DB = "du_an_ban_dat"

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

conn = connect()
# def create_user():
  
#   conn = connect()
#   query = "SELECT * FROM provinces where id = 1"
#   conn.execute(query)
#   #conn.close()
#   #data= 'kjj'
#   rows = conn.fetchone()
#   return rows
def create_user():
    try:
        cursor = conn.cursor(dictionary=True)
        db_query = cursor.execute("SELECT * FROM provinces where id = 1")
        row = cursor.fetchone()
        if row:
            return json.dumps(row)
        else:
            return "Nothing found \n SQL Query: " 
    finally:
        cursor.close()
def create_id():
    try:
        cursor1 = conn.cursor(dictionary=True)
        db_query = cursor1.execute("SELECT * FROM provinces where id = 2")
        row1 = cursor1.fetchone()
        if row1:
            return json.dumps(row1,cls=DateTimeEncoder)
        else:
            return "Nothing found \n SQL Query: " 
    finally:
        cursor1.close()
def infor_id():
    try:
          # Assume you have a function to connect to the database
        cursor = conn.cursor(dictionary=True)
        db_query = cursor.execute("SELECT * FROM infor_news ORDER BY id DESC LIMIT 10")
        rows = cursor.fetchall()
        if rows:
            return rows
        else:
            return "No records found."
    finally:
        cursor.close()
# def infor_id():
#     try:
#         cursor = conn.cursor(dictionary=True)
#         db_query = cursor.execute("SELECT * FROM infor_news ") #order by id DESC 10
#         row1 = cursor.fetchone()
#         if row1:
#             return (row1)
#         else:
#             return "Nothing found \n SQL Query: " 
#     finally:
#         cursor.close()
# def search_db_tickId_act(ticketId):
#     try:
#         cursor = db.cursor(dictionary=True)
#         db_query = cursor.execute("SELECT * FROM provinces where id = 1", ticketId)
#         row = cursor.fetchone()
#         if row:
#             return json.dumps(row)
#         else:
#             return "Nothing found \n SQL Query: " + "select * from active_predicted where ticketId=" + str(ticketId)
#     finally:
#         cursor.close()
  #rows = conn.fetchall()
  #return rows
# def create_user():
#   conn = connect()
#   cursor = conn.cursor()
#   query = "SELECT * FROM provinces"
#   conn.execute(query)
#   rows = conn.fetchall()
#   return rows