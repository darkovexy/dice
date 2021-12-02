# An attribute that belongs to the instance(object)
# Note: Instance attributes take preference over class attributes during 
# assignment and retrieval.
# Example:
class Employee:
    company = "Google"  # This is class attribute specific to each class.
    # company refered as attribute1 for understanding.

chinmay = Employee()
chinmay.company =  "Amazon" #Instance attribute.
print(chinmay.company)
# preference:
#chinmay.attribute1  :
# Is attribute1 present in the object?
# Is attribute1 present in class?
