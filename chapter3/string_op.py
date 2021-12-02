#String is a data type in python or any other programming languages.
#We can write string in a three ways 1.using 'strings',2.using "strings" 
# 3. using '''strings''' .We can use any of this ways according to the situation.
string1 = 'chinmay is a good boy. '
string2 = "and his friend's also smart and intelligent."
string3 ='''chinmay is a smart, intelligent and gentlemen and his 
 friend's also good and smart. '''

#String Operations
#in python using + symbol we can concatenate multiple strings.
concat = string1 + string2
print(concat)

#String Slicing
#A string in Python can be sliced for getting a part of the string.
#A string can be sliced by using its index value and in python index value starts from 0 to length-1.
eg = "Hi Chinmay"
print(eg[0:7])
#Some important points
eg[:7] #-->same as eg[0:7]
eg[0:] #--> same as eg[0: length of the string]
print(eg[0:])
#Sometimes we can use minus value also for slicing
print(eg[-10:-3]) #same as eg[0:7]

#Slicing with skip value
word = "GoodLuck chinmay"
print(word[0::2])#same as word[0:15:2] the last value is the skip value here.2 means after printing first word(in where slicing start) we need to print exact next second(bcz here the value 2 so we say second) word wrt to it previous word in the sequence till not completed the word(in where slicing ended) 
print(word[0:8:3])

#-------
#String Function