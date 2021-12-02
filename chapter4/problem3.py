#Check that a tuple cannot be changed in Python.
t = (1,2,3,4,5,"chinmay")
#Trying to change the value at index 2
t[2] = 45
print(t)