#Python offers a finally clause which ensures execution of a piece of code 
# irrespective of the exception.

try:
    n = int(input("Enter a number: "))
    a = n/1
    print(a)
except Exception as e:
    print("Value error occured make sure you entered an integer.")
    print("we are going to exit the program")
    exit()
finally:
    print("\nThis finally clause always executed regardless of the exception.\n we handle the exception and exit the program but this code is running.")