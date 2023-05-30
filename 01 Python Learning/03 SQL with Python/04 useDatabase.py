import mysql.connector as connector 

conn = connector.connect(host='localhost',
                         user='root',
                         passowrd='root',
                         database='pythontest') # using database

# this code will give error if we run it directly