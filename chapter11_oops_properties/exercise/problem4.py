#Write a class complex to represent complex numbers, along with overloaded 
# operators + and * which adds and multiplies them.

class Complex:
    
    def __init__(self,r,i):
        self.a = r
        self.b = i

    def __str__(self): # __str__ is used to print object directly.
        if self.b<0:
            return f"{self.a} - {- self.b}i"
        else:
            return f"{self.a} + ({self.b}i)"
    
    def __add__(self,obj2):
        x = self.a + obj2.a
        y = self.b + obj2.b
        return Complex(x,y)

    def __mul__(self,obj2):
        #real part calculation
        x = self.a*obj2.a - self.b * obj2.b
        #imaginary part calculation
        y = self.a * obj2.b + self.b * obj2.a
        return Complex(x,y)
c1 = Complex(5,-6)
c2 = Complex(4,3)

#Two complex number addition
sum = c1+c2
print(sum)

#Two complex number multiplication
mul = c1*c2
print(mul)