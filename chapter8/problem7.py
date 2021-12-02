#Write a python function to print the multiplication table of a given number.
n = int(input("Enter the number: "))
def multiplicationTable(num):
    print(f"Multiplication table for {num}")
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

multiplicationTable(n)