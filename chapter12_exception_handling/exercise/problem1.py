#Write a program to open three files 1.txt, 2.txt, and 3.txt. if any of these 
# files are not present, a message without exiting the program must be printed 
# prompting the same.

def fileread(filename):
    try:
        print(filename)
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")


file = "chapter12_exception_handling\exercise\\1.txt"
fileread(file)
fileread("3.txt")
fileread("2.txt")
# G: \Minor project-2021\chapter12_exception_handling\exercise\1.txt
