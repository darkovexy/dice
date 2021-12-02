# Inheritance is a oops property , which allows classes to inherit the 
# attributes and methods of another class. The class which is inherited from other class is called
# child class. The child class which is inherited from other class , 
# the other class is called paraent/base class.

class Animal:
    legs = 2
    eye = 2
    def run(self):
        print("Animal can run")
        
    def eat(self):
        print("Animal can eat")
    
class Dog(Animal): #Inherit the class Dog from Animal.
    
    def run(self): #This is called method overriding ,we rewrite the method of parent class.
        print("Dog can also run")
    def Bark(self):
        print("Dog can bark")

A = Animal() #Object of class A.
A.run() 
D = Dog() #Object of D
D.run()

print(D.legs) #Dog object access the Animal class attributes
D.legs = 4  # Here We are updating leg attribute value for Dog class.
print(D.legs)
print(A.legs)