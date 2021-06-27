import pickle

file = open('rollno.txt', 'wb')
dictionary = {1: 'Rohan', 2: 'Mohan', 3: 'Sohan', 4: 'Ram', 5: 'Shyam'}
pickle.dump(dictionary, file)
file.close()

file = open('rollno.txt', 'rb')
data = pickle.load(file)
print(data)

rn = int(input("Enter Roll. No. to be searched for: "))
try:
    print("The name of Roll. No. " + str(rn) + " is: ", data[rn])
except:
    print("The Roll. No. was not found.")

