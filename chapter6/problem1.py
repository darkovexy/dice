#Write a program to find the greatest of four numbers entered by the user.
n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
n3 = int(input("Enter the number3: "))
n4 = int(input("Enter the number4: "))

# if (n1>n2):
#     if (n1>n3):
#         if(n1>n4):
#            print("The greatest number is",n1)
#         else :
#            print("The greatest number is", n2)
#     else :
#         if(n3>n4):
#             print("The greatest number is", n3)
#         else :
#             print("The greatest number is", n4)
# else:
#     if (n2>n3):
#         if(n2>n4):
#             print("The greatest number is", n2)
#         else:
#             print("The greatest number is", n4)
#     else :
#         if(n3>n4):
#             print("The greatest number is", n3)
#         else :
#             print("The greatest number is", n4)

#Another solutions
if(n1>n2):
    f1 = n1
else:
    f1 = n2

if(n3>n4):
    f2 = n3
else:
    f2 = n4

if(f1>f2):
    print(f1," is greatest")
else:
    print(f2," is greatest")