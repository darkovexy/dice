# Write a program to display a/b where a and b are integers. If b=0, display
# infinite by handling the ZeroDivisionError.

a = int(input("Enter the value of a: "))
b = int(input("ENter the value of b: "))
try:
    c = a/b
    print(f"The result of a/b is {c}")
except ZeroDivisionError:
    print("Infinite")
