l=[]
n=int(input("Enter no of elemnts in the list: "))
for i in range(n):
    l.append(int(input("Enter Element: ")))
ans=0
for i in l:
    a=str(i)
    if a[len(a)-1]=='3':
        ans+=i
print("The sum of numbers ending with 3 is: ",ans)