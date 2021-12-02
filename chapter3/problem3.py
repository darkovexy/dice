#Write a program to detect double spaces in a string.
str1 = "hi  what are you  doing  ."
print(str1)
print("Total double spaces in the string is IN INDEX: ",str1.find("  "))

#Replace the double spaces from problem 3 with single spaces.
print(str1.replace("  "," "))