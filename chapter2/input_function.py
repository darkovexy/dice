# input() function:
# This function allows the user to take input from the keyboard as a string.
# Note: The output of the input function is always a string even if the number is entered by the user.

# Suppose if a user enters 34, then this 34 will automatically convert to “34” string literal.

a = input("Enter the number: ")
print(a , type(a))
a = int(a) # Convert a to an Interger.
print(type(a))