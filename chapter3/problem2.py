#Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|NAME|>,
Greetings from XYZ company,i am happy to tell you about your selection
you are selected!
Have a great day ahead!
Thanks and regards,

Date: <|DATE|>
'''
NAME = input("Enter the name:\n")
DATE = input("Enter a date(dd-mm-yy):\n")

letter = letter.replace("<|NAME|>",NAME)
letter = letter.replace("<|DATE|>", DATE)

print(letter)