#Write a class vector representing a vector of n dimension. Overload the + and 
# * operator which calculates the sum and the dot product of them.

class Vector:
    
    def __init__(self,vec): #we take vector as a list
        self.vec = vec
        
    def __str__(self):
        str1 =""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index+=1
        return str1[:-1] #slice string to remove extra add symbol in the last.
    
    #+ operator overload to perform vector addition
    def __add__(self,vec2):
        #If we add directly then two list merged so we can't do this.
        if len(self.vec) != len(vec2.vec):
            return "Add operation failed Because the dimension of the two vector is not same"
        
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return Vector(newList) 
        
    # * operator overload to perform vector multiplication
    def __mul__(self,vec2):
        if len(self.vec) != len(vec2.vec):
            return "Multiplication failed Because the dimension of the two vector is not same"
        
        sum  = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    

v1 = Vector([1,2,3])
v2 = Vector([4,5,8])
print(v1)
print(v2)
print(v1+v2)
print(v1*v2)
