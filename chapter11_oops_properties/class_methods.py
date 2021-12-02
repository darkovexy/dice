# A class method is a method which is bound to the class and 
# not the object of the class.

# @classmethod decorator is used to create a class method.

#IF we want to change class attribute directly not creating 
# any instance attribute then we can use class method.

class Employee:
    company = "Amazon" #class attribute
    salary = 5000      #class attribute
    location = "Mumbai"#class attribute
    
    # def changeSalary(self,sal):
    #     self.__class__.salary = sal # It is one method.
        # Dunder or magic methods in Python are the methods
        # having two prefix and suffix underscores in the method name. 
        # Dunder here means “Double Under
    
    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal
    

e = Employee()
print(e.salary)
e.changeSalary(10000)
print(e.salary)
print(Employee.salary)