# Write a program to print the third, fifth, and seventh elements from a list
# using the enumerate function.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, item in enumerate(list):
    if i == 2 or i == 4 or i == 6:
        print(f"The {i+1} th element is {item}")
