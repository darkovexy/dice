# In python we cannot have two method with same name in the same class.
# So we cannot achieve method overloading like we achieve in different language
# In python for method overloading we need to use default argument value.

class Number:
    
    def sum(self,x=None, y=None, z=None):
        if(x != None and y != None and z != None):
            sum = x+y+z
            print(sum)
        elif(x != None and y != None):
            sum = x+y
            print(sum)

n = Number()
n.sum(10,5)