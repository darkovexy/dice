#Some populer methods of list 
Friends = ["Biswa","Mriganka","Bhaskar","Sanjeev","Deepjyoti","47",False]
l2 = [45, 12, 39, True,5, 1, 13,True]
#The list can contain different types of elements such as int, float, string, #Boolean, etc. Above list is a collection of different types of elements.

#Methods
# Friends.sort()
# Sort method doesnot work between Bool and String
print(Friends)
l2.sort() #See the output its interesting
print(l2)

#Method no2
'''# Friends.reverse() #It will reverse the list
# print(Friends)'''

#Method no3
Friends.append("Rupak") #Add at last
print(Friends)

#Method no4
Friends.insert(5,46) #Insert at index 5 with 46.
print(Friends)

#Method no5
returnValue = Friends.pop(5)  # It will delete the element at index 5 and return its value
print(returnValue)

# Method no6
Friends.remove("Bhaskar") #it will remove Bhaskar from the list.
print(Friends)