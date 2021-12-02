#Create a class of pets from a class Animals and further create class Dog from 
# Pets. Add a method bark to class Dog.

class Animals:
    def run(self):
        print("Animal can run")
    def eat(self):
        print("Animals can eat")

class pets(Animals):
    
    def eat(self):
        print("Pets eat only milk")
        
        
class Dog(pets):
    
    def bark(self):
        print("Dog can bark.")
        

A1 = Animals()
P = pets()
D = Dog()

D.bark()
D.run()
D.eat()