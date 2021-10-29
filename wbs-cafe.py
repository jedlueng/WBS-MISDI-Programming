#Jedlueng 29 October 2021 


''' 
• WBS café is doing a promotion that whenever a customer is buying at least a cup of coffee, 
he/she can buy cookies at half the normal price. 
Can you write a Python program to calculate the total price a customer needs to pay?
• The normal price of a cup of coffee is £2
• The normal price of a bag of cookies is £1
• For example, a customer need to pay £5.5 (2 * 2 + 1 * 0.5 * 3) for a purchase of 2 cups of coffee and 3 bags of cookies.
• Sample output:
Please enter the number of cups of coffee: 2 Please enter the number of bags of cookies: 3 The total price is: £ 5.5
'''



user_in_coffee = int(input('Please enter the number of cups of coffee:'))
user_in_cookie = int(input('Please enter the number of bags of cookies:'))


if user_in_coffee > 0: 
    print('The total price is: {} £'.format(user_in_coffee+(user_in_cookie/2)))


