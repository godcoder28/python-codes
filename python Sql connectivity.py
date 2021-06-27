import mysql.connector
MyDb = mysql.connector.connect(user="root",
    password="12345", host="localhost", database="cs_practical")
cursor = MyDb.cursor()
cursor.execute('SELECT * FROM student WHERE name LIKE "Nishant"')
Data = cursor.fetchall()
MyDb.close()
print(Data)
