#random_game.py
#JedLueng 5 November 2021 

import random 

n = random.randint(1, 99)
guess = int(input(("Enter an integer from 1 to 99: ")))

while n != guess: 
    print('Guess Again mate')
    if guess < n:
        print('This is high mate')
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print('This is low mate')
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print('you guessed it! mate')
        break
    print('Yeah you good')


    