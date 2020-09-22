# WAP to input a list and perform Linear Search
# Made By: Shivang Gupta
li = []
n = int(input("Enter the No of elements: "))
for i in range(n):
    li.append(int(input("Enter an element: ")))
e = int(input("Enetr an element to be searched: "))
for i in range(n):
    if li[i] == e:
        print("The element ", e, " is in the list at position: ", i + 1)
        break
    if i == n - 1:
        print("The element is not present in the list.")
