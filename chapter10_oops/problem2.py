# Write a class calculator capable of 
# finding square, cube, and the square root of a number.

class Calculator():
    
    def __init__(self,num):
        self.num = num
    
    def square(self):
        result = self.num ** 2
        print(f"The square of the number is: {result}")
    
    def cube(self):
        result = self.num ** 3
        print("The cube of the number is: ",result)
    
    def squareRoot(self):
        sqrt = self.num ** 0.5 # If a number hv power 1/2 or 0.5 then it will represent to the square root of that number.
        print("The square root of the number is : ",sqrt)

n = int(input("Enter the number: "))
number = Calculator(n)

number.square()
number.cube()
number.squareRoot()