#Dictionary is a collection of key-value pairs.
#Properties of Python Dictionaries
# It is unordered
# It is mutable
# It is indexed
# It cannot contain duplicate keys
# In dictionary each key contains only one value againts it multiple values not  allowed.
# mydict = {
#   "name" : "chinmay,jyotirmoy" Wrong syntax.
# } 

#----------------------------------------
#creating dictionary using {}
myDict  = {
    "apple" : "name of a Fruit", #apple is key and "name of a fruit" is value.
    "Chinmay": "A coder", 
    "marks" :[4,7,9],# in dictionary we can add list also as a key -value pair.
    #One dictionary can contains multiple dictionary.
    #But here we need to use the syntax of key value pairs.
    "anontherDict" : {
        "language" : "Its a medium of communication"
    }
}

print(myDict["apple"]) #printing the value of key.
print(myDict["anontherDict"]["language"]) # Printing another dictionary value #of a pariticular key
print(myDict["marks"]) #printing the list.
print(myDict["marks"][1]) #Here accessing inside list items using index no. 

myDict["marks"] = [6,2,1] # Updating the value of the key.
print(myDict["marks"])
print(myDict) #printing complete dictionary.