file = open('data.txt', 'r')
data = file.read()
counter = 0
for i in data.replace('\n', '').replace(' ',''):
    counter += 1
print("Total No of characters are: ", counter)