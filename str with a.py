old_file = open("data_old.txt", "r")
data = old_file.readlines()
old_file.seek(0)
print(old_file.read(), '\n')

new_file = open("data_new.txt", "w+")
for i in data:
    if "a" in i:
        continue
    else:
        new_file.write(i)

new_file.seek(0)
print(new_file.read())
