def binary(array, element):
    n = len(array) - 1
    if len(array) > 0:
        if element == array[n // 2]:
            return l.index(array[n // 2]) + 1
        elif element > array[n // 2]:
            return binary(array[n // 2 + 1::], element)
        else:
            return binary(array[0:n // 2], element)
    else:
        return None


l = []
x = int(input("Enter no of elements in the list: "))
for i in range(x):
    l.append(int(input("Enter element: ")))
e = int(input("Enter element to be searched: "))
print("The list given is: ", l)
print("The element is found at position: ", binary(sorted(l), e))
