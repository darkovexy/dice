#Override the __len__() method on vector of problem 5 to display the dimension 
# of the vector.

class Vector:

    def __init__(self, vec):  # we take vector as a list
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        # slice string to remove extra add symbol in the last.
        return str1[:-1]

    #+ operator overload to perform vector addition
    def __add__(self, vec2):
        #If we add directly then two list merged so we can't do this.
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return Vector(newList)

    # * operator overload to perform vector multiplication
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

    # Question no 7 method 
    def __len__(self):
        return len(self.vec) # Here returning the dimension of the vector.

v1 = Vector([1, 2, 3,5])
v2 = Vector([4, 6, 8])
print(len(v1))
print(len(v2))