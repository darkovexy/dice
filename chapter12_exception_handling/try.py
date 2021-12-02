#There are many built-in exceptions that are raised in Python when something 
# goes wrong.
#Exceptions in Python can be handled using a try statement. The code that 
# handles the exception is written in except clause
# When the exception is handled, the code flow continues without program 
# interruption
# why we need to use exception handling?
# Without exception handling if the program has some errors then it will crash 
# the program and flow of the program stopped.If we use GUI after that if my 
# program throws error then GUI will be crashed To avoid this type of scenarie 
# we need to use exception handling concept in python.

print("Press q to exit of the program... ")
while True:
    a = input("Enter the number: ")
    if a == 'q':
        break
    
    try:
        print("Trying...")
        a = int(a)
        if a>6:
            print("Number is greater than 6")
            
    except Exception as e:
        print(e)

print("Thanks!")