import mysql.connector as connector

conn = connector.connect(host='localhost',
                         user='root',
                         password='root')

# creating cursors
cur = conn.cursor()

# writig queries
query = 'SHOW DATABASES'

# executing queries
cur.execute(query)

# displaying all databases
for i in cur:
    print(i)
