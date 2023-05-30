import mysql.connector as connector 

conn = connector.connect(host='localhost',
                         user='root',
                         password='root')

cur = conn.cursor()

db_name = input("Type database name: ")
query = f'CREATE DATABASE IF NOT EXISTS {db_name}'

cur.execute(query)

print(cur.rowcount, "database created.")