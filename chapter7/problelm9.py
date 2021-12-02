#Write a program to print the multiplication table of n using for loop in reversed order.
n = int(input("Enter the number : "))
for i in range(10,0,-1):
    print(f"{i} x {n} = {i*n}")