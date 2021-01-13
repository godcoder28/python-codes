file = open("data_old.txt", 'r')
counter = 0
for i in file.read().replace("\n", ' ').split(' '):
    if i == 'is':
        counter += 1
print("Total number of occurrences of is: ", counter)