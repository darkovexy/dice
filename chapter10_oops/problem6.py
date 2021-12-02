# Can you change the self parameter inside a class to 
# something else (say ‘harry’)? Try changing self to ‘slf’ or ‘harry’ and
# see the effects.

class Sample():
    def getName(self):
        print(self.name)
    def getAge(slf):
        print(slf.age) 
        print("Yes we can change the self parameter inside\n a class to something else \n But we never change it bcz if we change \n it is very difficult for other programers \nto understand our code ")
    
chinmay = Sample()
chinmay.name =  "CHinmay"
chinmay.age = 23
chinmay.getName()
chinmay.getAge()