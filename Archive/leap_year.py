#Jedlueng 29 October 2021 


user_input = int(input('Please enter the year:'))

next_leap_year = (user_input % 4)

# leap_year = [] 

# for i in range(1,5000):
#     if (i % 100 != 0) and (i % 4 == 0): 
#         leap_year.append(i)


if user_input % 100 != 0 and user_input % 4 == 0:
    print('Yeah this is a leap year')
else:
    print('This is not a leap year')
    print('{} years to next leap year.'.format(next_leap_year))
    



