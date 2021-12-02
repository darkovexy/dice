#Write a program to accept the marks of 6 students and display them in a sorted #manner.
s1 = int(input("Enter marks of the 1 student: "))
s2 = int(input("Enter marks of the 2 student: "))
s3 = int(input("Enter marks of the 3 student: "))
s4 = int(input("Enter marks of the 4 student: "))
s5 = int(input("Enter marks of the 5 student: "))
s6 = int(input("Enter marks of the 6 student: "))
studentMarks = [s1,s2,s3,s4,s5,s6]
studentMarks.sort()
print(studentMarks)
