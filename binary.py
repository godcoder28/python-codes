from random import *

l = []
for i in range(20):
    l.append(randint(0, 50))
l.sort()
print(l)


def binary(item, list):
    index = None
    while len(list) > 0:
        n = len(list)
        if item == list[n // 2]:
            index = l.index(list[n // 2]) + 1
            break
        else:
            if list[n // 2] > item:
                list = list[:(n // 2):]
            else:
                list = list[(n // 2) + 1::]
    return index


item = int(input("Enter item to be searched: "))
print("The given element is found at position: ", binary(item, l))
