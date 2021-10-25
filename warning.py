
#Jedlueng 22 October 2021 

'''Please enter the visitor's temperature: 38 
***********************************
**************WARNING**************
***HIGH TEMPERATURE 38C DETECTED***
***********************************'''


print('Please enter your temperature')

temp_lim = 37.5
temp = int(input())

if temp > temp_lim: 
    print('***********************************')
    print('**************WARNING**************')
    print('***HIGH TEMPERATURE '+str(temp)+'C DETECTED***')
    print('***********************************')



