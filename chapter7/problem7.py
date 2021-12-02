#Write a program to print the following star pattern.
#     *

#   ***  

# ***** for n=3

n = int(input("Enter the value of n: "))
# for i in range(1,n+1):
#     print(" " * 2*(n-i), end="") 
#     for j in range(n):
#         print("*" * (i+j))

#         #Wrong answers need to correct

for i in range(1,n+1):
    for j in range(1,(n+1)-1):
        print(" ",end="")
        for k in range(1,i+1):
            print("*",end="")
        print("\n")