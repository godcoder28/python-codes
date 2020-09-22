"""To print following patterns on screen:
 *
 **
 ***
 **** """
for i in range(4):
    for j in range(i + 1):
        print("*", end='  ')
    print("\n")
