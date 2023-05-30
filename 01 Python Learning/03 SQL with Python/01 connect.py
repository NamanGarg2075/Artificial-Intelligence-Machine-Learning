# pip install mysql-connector

import mysql.connector as coctr

conn = coctr.connect(
    host="localhost",
    user="root",
    password="root",
    )

if conn.is_connected():
    print("Connected to database")
else:
    print("Not connected")