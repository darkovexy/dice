## Write a program to input eight numbers from the user and display all the #unique numbers (once).

a  = set()
n1 = int(input("Enter the 1Number: "))
a.add(n1)
n2 = int(input("Enter the 2Number: "))
a.add(n2)
n3 = int(input("Enter the 3Number: "))
a.add(n3)
n4 = int(input("Enter the 4Number: "))
a.add(n4)
n5 = int(input("Enter the 5Number: "))
a.add(n5)
n6 = int(input("Enter the 6Number: "))
a.add(n6)
n7 = int(input("Enter the 7Number: "))
a.add(n7)
n8 = int(input("Enter the 8Number: "))
a.add(n8)

##2nd solution
#Instead of add we can directly create a set with 8numbers.
#a = {n1,n2,n3,n4,n5,n6,n7,n8}

print("All the unique numbers is: ",a)