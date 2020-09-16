import random
print ('number guessing game')
number=random.randint(1,9)
chances=0
print('guess a number between 1 to 9')
while chances<5:
    guess=int(input('enter your guess'))
    if guess==number:
        print('congratulations you have won')
        break

    elif guess<number:
        print('guess a higher number')

    else:
        print('guess a lower number')

    chances=chances+1
    if not chances<3:
        print('you lose and the number is',number) 

input(' press enter to exit')                   