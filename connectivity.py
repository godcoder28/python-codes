import mysql.connector
MyDb = mysql.connector.connect(user="root", password="12345", host="localhost",
                               database="coder01")
cursor = MyDb.cursor()

cursor.execute('SELECT * FROM agents')
data = cursor.fetchall()
print("OLD Data:")
for i in data:
    print(i)
    
cursor.execute('UPDATE agents SET working_area = "Delhi" WHERE agent_code = "A007"')
cursor.execute('DELETE FROM agents WHERE agent_code = "A012"')
MyDb.commit()

cursor.execute('SELECT * FROM agents')
data = cursor.fetchall()
print("NEW Data:")
for i in data:
    print(i)
MyDb.close()

