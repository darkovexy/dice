#A number can be converted into a string and vice versa (if possible)
#There are many functions to convert one data type into another.THis process is #called typecasting
#example

a = "234" #in this stage its a string literal

# type function is used to find the data type of a given variable in Python.
print(type(a))

a = int(a) #Here we int function trying to convert a into integer.(success = not always 100%) ,in this stage its called numeric literal.
print(type(a))
a = float(a)
print(a, type(a))

#Lets see some unsuccessful typecasting

b = "34safds56"
b = int(b) #This gives us an error here casting failed.
print(type(b))