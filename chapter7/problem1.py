# Write a program to print the multiplication table of a given 
# number using for loop.

num = int(input("Enter the number: "))
for i in range(1,11):
    print(str(num)+" X "+str(i) +" = "+str(num*i))
print("\n\n\n")

# str() is used to convert the number into string.

#We can use f string for the above problem.
# We can use f string when we need to do some calculation for numbers.
# in middle of the string or when we want to print number and string together
# without typecasting bcz it is easier to use .
# in f string we need to use { } for variables nd we can do calculation under  # curly brackets its allowed in python.
# How to use f string ?  

print("Using f string:\n")
num = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
