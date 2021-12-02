#Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
sub1 = int(input("Enter the marks of the subject1: "))
sub2 = int(input("Enter the marks of the subject2: "))
sub3 = int(input("Enter the marks of the subject3: "))

total_percent = ((sub1+sub2+sub3)/300)*100

if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed !")
elif(total_percent<40):
    print("You are failed due to scoring less than 40% in total percentage.")
else:
    print("Congrats you have passed the exam!")