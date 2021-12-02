#Write a recursive function to calculate the sum of first n natural numbers.

num = int(input("Enter the number: "))

def sumOfNaturalNo(num):
    if num >0 :
        return num + sumOfNaturalNo(num-1)
    else:
        return num

print(sumOfNaturalNo(num))
