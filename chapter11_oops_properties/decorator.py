class Employee:
    company = "Hondai"
    salary = 8000
    salaryBonus = 800
    #totalSalary = 8800 , #if we hard code like this then we may need to face 
    #lots of problems like if the salary bonus increases then we need to 
    # hard code total salary again. We can solve this problem using getter 
    # and setter decorator.We can use the totalSalary as a function internally
    # but externally we can access it as property of a class.
    
    # The method name with @property decorator is called getter method.
    @property
    def totalSalary(self):
       return self.salary + self.salaryBonus

    @totalSalary.setter #this is setter method ,if we change totalSalary property
    # directly then we need to update the salaryBonus automatically so that it will
    # balance.Thats why we use setter method.
    def totalSalary(self,val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)
print("\n")
e.totalSalary = 10000 #We are changing the totalSalary.
print(e.salary)
print(e.salaryBonus)