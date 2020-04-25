#Input value of a,b & cand solve the quadratic equasion based of the input?
#Date: 9/7/19
a=int(input("Enter 'a':"))
b=int(input("Enter 'b':"))
c=int(input("Enter 'c':"))
if (b**2-(4*a*c))<0:
    print("The roots are imaginary")
elif (b**2-(4*a*c))==0:
    print ("the roots are same and equal to:",(-1*b)/2*a)
else :
    sol=((-1*b)+(b**2-(4*a*c))**0.5)/2*a
    sol2=((-1*b)-(b**2-(4*a*c))**0.5)/2*a
    print ("The 2 roots of the equation are:",sol ,"and" ,sol2)

