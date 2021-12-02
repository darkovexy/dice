# The enumerate function adds counter to an iterable and returns it.

list1 = [4,39,"chinmay",True]

# Normally prints the list .
# for item in list1:
#     print(item) 

#Using enumerate function 
for i,item in enumerate(list1):
    print(item,i) #Prints item and its index value ,here order we can change 