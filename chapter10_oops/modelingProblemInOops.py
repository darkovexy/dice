'''
We need to identify the following:

Noun--->Class--->Emplyoee(example)
Adjective---> Attributes ---> name,age,salary
Verb ---> Methods ---> getSalary(),increment()

'''

# simple Example

class Employee : 
    #define the attribute and assign none value.
    
    age = None
    department = None
    salary = None
    def getSalary(self):
         return self.salary

chinmay = Employee()
chinmay.salary = 50000
chinmay.age = 25
chinmay.department = "Senior software developer"

# print(chinmay.getSalary())
chinmay_salary = chinmay.getSalary() #This is equivalent to Employee.getSalary(chinmay)
print(chinmay_salary)