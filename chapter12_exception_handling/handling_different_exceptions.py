try:
    n = int(input("Enter a integer: "))
    a = 1/n
    print(a)
    
except ValueError as e:
    #print(e)
    print("Please enter a valid input.")
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero.")
except : #All other exceptions are handled here.
    pass