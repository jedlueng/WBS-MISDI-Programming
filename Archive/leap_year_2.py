#Jedlueng 


''' Write a program to find out all the leap years between year AD 1 and the year specified by the user via input, 
and print out these years and the total number of leap year.
 You can use condition statement from earlier exercise to check 
 if a given year is a leap year.'''



user_input = int(input('Which end year do you want to find?'))

list_leap_year = [] 
for i in list(range(1, user_input)): 
    if i % 100 != 0 and i % 4 == 0: 
        # print(i)
        list_leap_year.append(i)



print(list_leap_year)



