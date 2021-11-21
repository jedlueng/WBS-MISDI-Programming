#Jedlueng 12 November 2021 


'''
Please write a Python program to check the validity of the password entered by users. Please try to solve this with what has been covered so far.

Rules:
1.At least 1 letter between [a-z] and 1 letter between [A-Z]. 2.At least 1 number between [0-9].
3.At least 1 character from [$#@].
4.Minimum length 6 characters.
5.Maximum length 16 characters.




'''



import re
password = input("Type your password")
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
  
if flag ==-1:
    print("Not a Valid Password")
