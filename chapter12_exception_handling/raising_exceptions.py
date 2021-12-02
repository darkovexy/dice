# we can raise custom exceptions using the raise keyword in python.

def increment(n):
    try:
        return int(n)+1
    except:
        raise ValueError("You entered a wrong value.") # raise error must be meaningful.
    # syntax:
    # try:
    #    statement
    # except:
    #   raise CustomErrorName("Customize error description!")       
n = input("Enter a value: ")
a = increment(n)
print(a)