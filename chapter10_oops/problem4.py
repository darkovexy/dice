# Add a static method in problem 2 to greet the user with hello.

class Calculator():

    def __init__(self, num):
        self.num = num

    def square(self):
        result = self.num ** 2
        print(f"The square of the number is: {result}")

    def cube(self):
        result = self.num ** 3
        print("The cube of the number is: ", result)

    def squareRoot(self):
        # If a number hv power 1/2 or 0.5 then it will represent to the square root of that number.
        sqrt = self.num ** 0.5
        print("The square root of the number is : ", sqrt)

    @staticmethod
    def greet():
        print("Hello Chinmay! This is problem no 4")

n = int(input("Enter the number: "))
number = Calculator(n)

number.square()
number.cube()
number.squareRoot()
number.greet()