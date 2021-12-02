#Create a class with a class attribute a; create an object from it and 
# set a directly using object.a=0 Does this change the class attribute?

class Attribute():
    a = 1 #Take as assumption # class attribute
    
obj = Attribute() #Create an object of a class Attribute
obj.a = 0 #Trying to change the value of class attribute using object of that class.
# Here new obj attribute will be created which name is a.

if Attribute.a == 1 :
    print("We cannt change the class attribute using objct.")
else:
    print("Successfully changed")