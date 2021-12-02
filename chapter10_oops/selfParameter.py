# In python self refers to the object(instance) of the class.
# Simple example



class Employee:
    company = "Google"
    
    def getSalary(self): # Here self is chinmay the object who called the getSalary().
        print("Salary is not there")
        
chinmay = Employee() # Here creating object, chinmay is the object of the class Employee.
chinmay.getSalary() # Here we are  passing 1 argument.
# above lines of code is equivalent to 
# Employee.getSalary(chinmay)