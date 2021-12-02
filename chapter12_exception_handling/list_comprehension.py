# List comprehension is an elegant way to create lists based on existing list.
# we can also do set comprehension/dictionary comprehension.
items = [1,2,3,4,54,45,68,95,781,255]
# list2 = []

# for item in items:
#     #Creating new list which contains only even numbers.
#     if item % 2 == 0: 
#         list2.append(item)

# print(list2)

#Shortcut to write the same:
list2 = [ i for i in items if i%2 == 0] # first i is the value which is stored in the new list.
print(list2)