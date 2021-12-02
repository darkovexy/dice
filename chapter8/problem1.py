#Write a program using the function to find the greatest of three numbers.

n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
n3 = int(input("Enter the number3: "))

def greatest(num1,num2,num3):
    if(num1 > num2):
        n = num1
    else:
        n = num2
    if(n > num3):
        return n
    else:
        return num3

print("Greatest is: ",greatest(n1,n2,n3))