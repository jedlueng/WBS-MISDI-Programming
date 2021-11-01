year = int(input('num'))



if year % 4 == 0: 
    print('Leap')
elif year % 100 == 0 and year % 400 == 0:
    print('Leap')
else: 
    print('NOt leap')


