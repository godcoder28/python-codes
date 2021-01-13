file = open("data_old.txt", 'r')

for i in file.readlines():
    print(i.replace(' ', ' # ').replace('\n', ' # '), end='')