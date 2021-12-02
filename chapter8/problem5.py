# Write a python function that converts inches to cms.

def inchToCm(inch):
    return inch * 2.54

inch  = float(input("Enter the value of inch: "))

print(str(inchToCm(inch)))