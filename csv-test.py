import csv
file = open("student.csv", 'r')
reader = csv.reader(file)

for i in list(reader):
    print(i)

file.close()
  
