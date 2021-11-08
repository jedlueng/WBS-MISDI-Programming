#JedLueng 5 November 2021 


#This program calculate commission of the sales person 

# 0 - 100k == 10%
# 100k - 200k == 7.5% 
# 200k - 400k == 5%
# 400k - 600k == 3% 
#600k - 1m == 1.5% 
#above 1m == 1% 


money = int(input('How much do you make?'))
if money > 1000000: 
    print('Your commision is {}'.format(money*0.01))
elif money < 1000000 and money > 600000: 
    print('Your commision is {}'.format(money*0.015))
elif money < 600000 and money > 400000:
    print('Your commision is {}'.format(money*0.03))
elif money < 400000 and money > 200000: 
    print('Your commision is {}'.format(money*0.05))
elif money < 200000 and money > 100000:
    print('Your commision is {}'.format(money*0.075))
else: 
    print('Your commision is {}'.format(money*0.1))




