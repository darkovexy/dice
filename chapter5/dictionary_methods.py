myDict = {
    "apple": "name of a Fruit",  # apple is key and "name of a fruit" is value.
    "Chinmay": "A coder",
    # in dictionary we can add list also as a key -value pair.
    "marks": [4, 7, 9],
    #One dictionary can contains multiple dictionary.
    #But here we need to use the syntax of key value pairs.
    "anontherDict": {
        "language": "Its a medium of communication"
    },
    1 : 3 #Here integer is key and value.
}

# Dictionary Method
print(myDict.keys()) #prints keys of the dictionary
print(myDict.values()) #prints the values of the dictionary.
print(myDict.items()) #print the (key, value)for all contents of the dictionary.

print(myDict)
updateDict = {
    "Roll no" : "csm20039",
     1 : 5
}

myDict.update(updateDict) #Updates the dictionary by adding key value pairs from updateDict.
print(myDict)

print(myDict.get("Chinmay")) #prints values associated with the key "Chinmay"
print(myDict["Chinmay"])   # prints values associated with the key "Chinmay"

#Difference between .get and [] syntax in dictionaries?
print(myDict.get("Chinmay2")) #Returns none as "Chinmay2" is not present in the dictionary.
print(myDict["Chinmay2"]) #Throws an error as "Chinmay2" is not present in the dictionary.