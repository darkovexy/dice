# An attribute that belongs to the class rather than a particular object.
# Example
# We define class attributes outside all the methods, usually 
# they are placed at the top, right below the class header.
class Employee:
    company = "Google" # This is class attribute specific to each class.
    
chinmay = Employee() #object instantiation
print(chinmay.company) # Accessing class attribute
print(Employee.company) # We can access class attribute via a instance or via the class name.

Employee.company = "Youtube" # If we want to change the value of the class attribute 
# we can only use className.attributeName
print(chinmay.company)