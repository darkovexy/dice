#A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a #program to detect these spams.

##Solution1

text = input("Enter the comment:\n")

if("make a lot of money" in text): # in is used to check the word is present in #the text or not.
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("Text is spam!")
else:
    print("Text is not spam.")