# Write a python function to print the first n lines of the following pattern.
# ***

# **  # For n = 3

# *

n = int(input("ENter the value of n: "))

def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print("\n")

pattern(n)
