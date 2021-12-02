#Write a python program using the function to convert Celsius to Fahrenheit.

def celsius(F):
    C = 5/9 *(F - 32)
    return C

F = int(input("ENter the value of the temperature: "))
print("The celsius value is ",celsius(F))