# Global variable implementation

a = 45
def fun():
    global a #Now we can change the  value of global variable inside the function.
    print("The statement 1: ",a)
    a = 6 #Here we set the value of a locally that means we can't access
    # value 6 outside of the fun().
    print("The statement 2: ",a) #Local variable value display.
    
fun()
print("The statement 3 : ",a) #Here displaying the value of global variable.