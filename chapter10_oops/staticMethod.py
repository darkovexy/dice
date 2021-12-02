# Sometimes we need a function that doesnot use self parameter.
# We can define a static method like this
# syntax:
# @staticmethod
# def func():
#      statement

class Employee:
    company = "Google"
    
    def getSalary(self): 
        print("Salary is not there")
        
    @staticmethod
    def greet():
        print("Good moring sir!!")
        
chinmay = Employee() 
chinmay.getSalary()
chinmay.greet() #Here we dont pass any parameter bcz greet() defined as static method.