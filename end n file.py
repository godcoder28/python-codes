file = open('data.txt', 'r')
data = file.readlines()
for i in data:
    if i.replace('\n','')[-1] == 'n':
        print(i.replace('\n', '' ))
