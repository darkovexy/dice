a = 36
b = 12

# Arithmetic operator
print("the value a+b is",a+b)
print("the value a-b is",a-b)
print("the value a*b is",a*b)
print("the value a/b is",a/b) #In python /(devision) gives always float number.

# Assignment Operator
c = a+b
print(c)
a+=4 #This is the shortcut of addition in any single operator
print(a)
a-=10#same but here substraction
print(a)
a*=2 # here multiplication
print(a)
a/=10 # here devision
print(a)

#Comparison Operator
#Let us two values value1 and value2
value1 = 10
value2 = 5
print(value1>value2)
print(value2 >= value1)
print(value2 <= value1)
print(value1 != value2)

#Logical Operator( and , or , not)

bool1 = True
bool2 = False
print("the value of bool1 and bool2 is ", (bool1 and bool2))
print("the value of bool1 or bool2 is ", (bool1 or bool2))
print("the value of not bool2 is ", (not bool2)) # In not operator works only on single operator.
