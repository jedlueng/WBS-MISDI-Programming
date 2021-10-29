#Jedlueng 28 October 2021 

''' Write a program using input() funciton 
and arithmetic operators 
to do the following tasks 

1) Obtain two interger inputs from users: X and Y
2) print out the last digit of X + Y 
'''



#Obtain two integer 


user_x = abs(int(input('User X please type your integer')))
user_y = abs(int(input('User Y please type your integer')))

# print(user_x)
# print(user_y)

# print(str(user_x[-1])+str(user_y[-1])) 


#Change int to str 

user_x_str = str(user_x)
user_y_str = str(user_y)


# + last two digits 
combine_x_y = int(user_x_str[-1]) + int(user_y_str[-1])


print(combine_x_y)