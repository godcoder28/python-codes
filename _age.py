"""To input a student’s marks in three subjects (out of 100) and prints the sum and percentage of marks.
Also, print the grade based on the table given below.
Percentage	Grade
         >=90	                    A1
>=80 and <90	A2
>=70 and<80	B1
>=60 and <70	B2
>=50 and <60	C
>=40 and <50	D
         <40	                    E  """
m1=float(input("Enter the Marks: "))
m2=float(input("Enter the Marks: "))
m3=float(input("Enter the Marks: "))
p=int((m1+m2+m3)/3)
print("Sum of marks is: ",m1+m2+m3,"and the Percentage is: ",p,"%",'\n',"The Grade is: " )
if p>=90:
    print('A1')
elif p>=80:
    print('A2')
elif p>=70:
    print('B1')
elif p>=60:
    print('B2')
elif p>=50:
    print('C')
print('D') if p>=40 else print('E')
    
