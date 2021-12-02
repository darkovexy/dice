#Write a program to find whether a given username contains less than 10 #characters or not.
username = input("Enter the username:\n")
if(len(username)<10):
    print("The string contains less than 10 characters.")
else:
    print("The string contains more than 10 character.")