#Some useful functions in strings
story = "once upon a time there was a university student name called Chinmay, who have started to learning python in his 3rd semester of MCA onwards from the youtube channel name called by CodeWithHarry"

#String function
print(len(story)) #len prints the length of the entire string.
print(story.endswith("rry")) #returns truth or false .

# It counts the total number of occurrences of any character.
print(story.count("o"))
# This function capitalizes the first character of a given string.
print(story.capitalize())
print(story.find("t")) #This functions finds a word and returns the index of the first occurences of that word in the string.
print(story.replace("called","addressedBy")) #This function replaces the old word with the new word in the entire string.




# strip()
string = "   hello this is chinmay    "
print(string)
print(string.strip()) #this function removes all the extra spaces in a string.