# Sometimes we want to run a piece of code when try was successful

try:
    n = int(input("Enter your age: "))
    
except Exception as e:
    print(e)
else:
    #This block code executed only if the try was successful.
    print("This code is run because try block was successfully run.")
    if n>18:
        print("You are an adult.")
    else:
        print("You are a child go and play football!")