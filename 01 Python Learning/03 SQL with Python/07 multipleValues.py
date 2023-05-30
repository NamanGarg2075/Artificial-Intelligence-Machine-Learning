import mysql.connector as connector 

conn = connector.connect(host='localhost',
                         user='root',
                         password='root',
                         database='pythontest')

cur = conn.cursor()

query = '''INSERT INTO employee(id,name,phone_no)
            VALUES 
                (%s,%s,%s) # this will take values from 'value'
'''

values = [(2,"Ayush",80000),
          (3,"Gupta ji",76800),
          (4,"Sharma ji", 68097)]


cur.executemany(query,values)

# without commit no changes will happen
conn.commit()

print(cur.rowcount, "records inserted.")