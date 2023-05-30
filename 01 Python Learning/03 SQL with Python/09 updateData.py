import mysql.connector as connector 

conn = connector.connect(host='localhost',
                         user='root',
                         password='root',
                         database='pythontest')

cur = conn.cursor()

table_name = input("Enter table name: ")
query = f'''UPDATE {table_name}
            SET phone_no=phone_no + 10
            WHERE phone_no >= 70000'''

cur.execute(query)
conn.commit()

print(cur.rowcount, "wors effected.")