#where the type or the class of an object is less important than the method it 
# defines. Using Duck Typing, we do not check types at all. Instead, we check 
# for the presence of a given method or attribute.

# THe name duck typing comes from the phrase:
# "If it looks like a duck and quacks like a duck,it's a duck."
# Types of polymorphism

class Duck:
    def sound(self):
        print("Quack quack")
    
class Dog:
    def sound(self):
        print("bhow bhow")

class Cat:
    def sound(self):
        print("Meow Meow")

def All_sound(obj):
    obj.sound()

x = Duck()
All_sound(x)
