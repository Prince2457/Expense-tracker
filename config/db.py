from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import os

load_dotenv()
DB_CONFIG ={
    'host':os.getenv("DB_HOST"),
    'user':os.getenv("DB_USER"),
    'password':os.getenv("DB_PASSWORD"),
    'database':os.getenv("DB_NAME")
}

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("connection connected successfully")
            return connection
        
    except Error as e: 
        print(f"failed connecting to database{e}")
        return None


def close_connection(connection, cursor):
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
    print("Connection Closed")        