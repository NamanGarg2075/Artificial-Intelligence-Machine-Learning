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

values = (1,"Naman Garg",98765)

cur.execute(query,values)

# without commit no changes will happen
conn.commit()

print(cur.rowcount, "record inserted.")