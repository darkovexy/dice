#Write a program that finds out whether a given name is present in a list or #not.
names = ["chinmay","hirak","mridu","mriganka","biswa"]
name = input("Enter the name to check\n")
if name in names:
    print("The name is present in the list")
else:
    print("The name is not present in the list")
