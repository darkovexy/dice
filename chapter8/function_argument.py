# A function can also takes some values as a argument
# we can pass the value in the paranthesis 
 
def greet(name) : 
    print("Hello " + name)

greet("chinmay") # chinmay is passed to greet in name.


#A function can also have default parameter value. 

def greet2(name = "stranger"):  #Here name has a default parameter value which is used when no value passed in the greet2.
    print("Good morining "+ name)


greet2("chinmay") 
greet2() #we r not passed anything in the greet2.Thats why default value of the name will print.