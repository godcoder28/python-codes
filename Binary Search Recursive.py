import random


def binary(list, element):
    n = len(list) - 1
    if len(list) > 0:
        if element == list[n // 2]:
            return l.index(list[n // 2]) + 1
        elif element > list[n // 2]:
            return binary(list[n // 2 + 1::], element)
        else:
            return binary(list[0:n // 2], element)
    else:
        return None


l = []
for i in range(10):
    l.append(random.randint(1, 100))
l.sort()
print(l)

item = int(input("Enter item to be searched: "))
print("Element found at: ", binary(l, item))
