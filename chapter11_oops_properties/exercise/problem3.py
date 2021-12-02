#Create a class Employee and add salary and increment properties to it.
#Write a method SalaryAfterIncrement method with a @ property decorator with a 
# setter which changes the value of increment based on the salary.

class Employee:
    salary = 1000
    increment = 1.5
    @property
    def SalaryAfterIncrement(self):
           return self.increment * self.salary
       
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,sai):
        self.increment = sai/self.salary
        
    
e = Employee()
print(e.SalaryAfterIncrement)

print(e.increment)
e.SalaryAfterIncrement = 2000
print(e.increment)