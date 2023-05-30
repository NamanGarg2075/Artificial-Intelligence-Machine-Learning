import mysql.connector as connector 

conn = connector.connect(host='localhost',
                         user='root',
                         password='root',
                         database='pythontest')

cur = conn.cursor()

table_name = input("Enter table name: ")

query = f'''CREATE TABLE {table_name}(
                id VARCHAR(255),
                name VARCHAR(255),
                phone_no INT
)'''

cur.execute(query)

print(cur.rowcount, "table created.")