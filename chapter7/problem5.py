#Write a program to find the sum of first n natural numbers using a while loop.
n = int(input("Enter total no of natural nos: "))
while(n>0):
    sum = (n*(n+1))//2
    break;
print(f"The sum of first {n} natural numbers is ",sum)