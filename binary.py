from random import *

array = []
for i in range(20):
    array.append(randint(0, 50))
print(array)
array_sorted = sorted(array)  # sorting a random list created above


def binary(item, list):
    index = None  # declaring a variable 'index' as none
    while len(list) > 0:  # base case for the loop to stop when list becomes empty
        n = len(list)
        if item == list[n // 2]:  # to check if element is the middle one
            index = array.index(list[n // 2]) + 1
            """return index of the element from the original list by using .index 
                      method and providing the middle element of our sorted list as argument"""
            break
        else:
            if list[n // 2] > item:
                list = list[:(n // 2):]
            else:
                list = list[(n // 2) + 1::]  # slicing list to lower or upper half depending on the middle element
    return index


element = int(input("Enter item to be searched: "))
print("The given element is found at position: ",
      binary(element, array))  # function call which returns index of element
# and returns none if element is not present
