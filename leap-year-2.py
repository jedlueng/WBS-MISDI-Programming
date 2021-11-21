#Jedlueng 12 November 2021 

'''
Write a program to find out all the leap years in a time period (for example, 2001 to 2100)
and store your results in a list. You can reuse script from earlier week's exercise 
to identify all the leap years in a time period.


'''

# Python program to check if year is a leap year or not


from_int = int(input('Please input from'))
to = int(input('Please put the end'))

leap_year_list = [] 

for i in range(from_int,to):
    if i % 4 == 0: 
        if i % 100 == 0: 
            if i % 400 == 0: 
                leap_year_list.append(i)
    else: 
        continue


print(leap_year_list)





