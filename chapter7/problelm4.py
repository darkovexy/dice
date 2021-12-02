#Write a program to find whether a given number is prime or not.
n = int(input("Enter the number: "))
prime = True
if n==1:
    prime = False
else : 
    for i in range(2,n):
        if(n%i == 0):
            prime = False
            break
if prime == False : 
    print("The number is not prime")
else:
    print("The number is prime")
