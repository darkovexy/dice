## Create an empty dictionary. Allow 4 friends to enter their favorite language #as values and use keys as their names. Assume that the names are unique.
#This solution is not proper correct as per qsn.
# myDict = {}
# friend1 = input("Friend1 Enter your name: ")
# language1 = input("What is your fav language: ")
# friend2 = input("Friend2 Enter your name: ")
# language2 = input("What is your fav language: ")
# friend3 = input("Friend3 Enter your name: ")
# language3 = input("What is your fav language: ")
# friend4 = input("Friend4 Enter your name: ")
# language4 = input("What is your fav language: ")

# frndDict = {
#     friend1 : language1,
#     friend2 : language2,
#     friend3 : language3,
#     friend4 : language4
# }
# myDict.update(frndDict)
# print(myDict)

favLang = {}
a = input("ENter your fav language Biswa:\n")
b = input("ENter your fav language mriganka:\n")
c = input("ENter your fav language Nitul:\n")
d = input("ENter your fav language Arnab:\n")

favLang["Biswa"] = a
favLang["mriganka"]= b
favLang["nitul"] = c
favLang["Arnab"] = d

print(favLang)