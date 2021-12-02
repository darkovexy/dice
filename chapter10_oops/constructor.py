# __init__() is a special method which runs as soon as object is created.
# This method is also known as constructor.
# It takes 'self' as a argument and also takes further arguments.
# This method is used when object is needed default intialization.


class Employee :
    company = "Google" # class attribute
    
    def __init__(self,name,age,salary):
        print("When object is created this constructor/method is automatically called.")
        self.name = name
        self.age = age
        self.salary = salary
        
    def getDetails(self):
        print(f"The name of the employee is : {self.name}")
        print(f"The age of the employee is : {self.age}")
        print(f"The salary of the employee is : {self.salary}")
        
        
    @staticmethod
    def greet(): #Static method dont need self argument.
        print("Good morning chinmay")
    
#object chinmay is created for the class Employee.
#chinmay = Employee() # ---> This gives us error bcz constructor need 3 argument.
chinmay = Employee("CHINMAY",23,"50k")
chinmay.greet()
chinmay.getDetails()
