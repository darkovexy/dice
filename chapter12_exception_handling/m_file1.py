# The file name start with m because in python if we want to import the file/
# program/as a module in another program then we need to set the file name 
# which is start with m. 

def greet(name):
    print(f"Good morning, {name}\n")

#__name__ evaluates to the name of the module in Python from where the program 
# is ran.
#If the module is being run directly from the command line, the __name__ is 
# set to string “__main__”.
#Thus this behavior is used to check whether the module is run directly or 
# imported to another file.

# print(__name__) 
if __name__ == '__main__':
    name = input("ENter a name: ")
    greet(name)
