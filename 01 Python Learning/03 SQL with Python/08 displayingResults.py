import mysql.connector as connector 

conn = connector.connect(host='localhost',
                         user='root',
                         password='root',
                         database='pythontest')

cur = conn.cursor()

table_name = input("Enter table name: ")
query = f'''SELECT * FROM {table_name}'''

cur.execute(query)

# fetching all results
results = cur.fetchall()

# to fetch all -> fecthall() 
# to fetch one row -> fetchone()

# printing all results
for i in results:
    print(i)

print(cur.rowcount, "wors effected.")