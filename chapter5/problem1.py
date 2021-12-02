##Write a program to create a dictionary of Hindi words with values as their #English translation. Provide the user with an option to look it up!
myDict = {
    "pankha" : "fan",
    "vastu" : "item",
    "kela" : "banana",
    "tormoj" : "watermelon"
}
print("Options are:\n",myDict.keys())
a= input("Enter the Hindi word:\n")
# print("Meaning of your word: ",myDict[a])
print("Meaning of your word: ", myDict.get(a))
