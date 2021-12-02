#Create a class programmer for storing information of a few programmers
# working at Microsoft.

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,age,salary,position):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position
    
    def displayInformation(self):
        print(f"{self.name} is a programmer,getting the salary {self.salary},who work as a {self.position} at the age of {self.age}. ")
    

programmer1 = Programmer("Chinmay",23,"1.5L","Software Developer")
programmer1.displayInformation()
programmer2 = Programmer("Manab Saha", 23, "1.5L", "Software Developer")
programmer2.displayInformation()