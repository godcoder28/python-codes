# WAP to input a list and perform Binary Search
# Made By: Shivang Gupta
li = []
n = int(input("Enter the No of elements: "))
for i in range(n):
    li.append(int(input("Enter an element: ")))
e = int(input("Enter an element to be searched: "))
l2 = sorted(li)


def bin(arr, item):
    while True:
        mid = int(len(arr) / 2)
        if arr[mid] == item:
            return (arr[mid])
        if len(arr) == 1:
            return (False)
        arr = arr[:mid] if arr[mid] > item else arr[mid + 1:]


if bin(l2, e) == False:
    print("The element is not in the list.")
else:
    print("The item is found at position: ", li.index(bin(l2, e)) + 1)
