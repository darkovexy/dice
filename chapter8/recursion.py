# Recursion is a function which calls itself.

# It is used to directly use a mathematical formula as a function

n = int(input("Enter the number: "))
def factorial(n):
    if(n == 0 or n == 1):
            return 1
    else:
        return n*factorial(n-1)

print(factorial(n))

# How recursion works
# factorial(4) function called 
# 4* factorial(3)
# 4 * 3* factorial(2)
# 4 * 3* 2 * factorial(1)
# 4*3*2*1 function returned
