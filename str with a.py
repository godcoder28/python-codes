old_file = open("data_old.txt", "r")
data = old_file.readlines()

new_file = open("data_new.txt", "a+")
for i in data:
    if "a" in i:
        continue
    else:
        new_file.write(i)

new_file.seek(0)
print(new_file.read())