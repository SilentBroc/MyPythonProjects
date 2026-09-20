import random

print('C0NGRAGULATIONS! You just captured a new country!')

user_country = input('What do you want to name your country\n')
user_population = input('How much people do you want to live in ' + user_country + '??\n')
enemy = input('WH0 IS Y0UR ENEMY??\n')

print('PLEASE CUT THE RED RIBBON T0 MAKE', user_country, '0FFICIAL!!!')
print('PRESS ENTER TO CUT THE RIBBON\n')
input()


print('OH NO!!!')
print('S0MEONE HAS PLACED A BOMB IN YOUR COUNTRY')
print('I COULD COMMINCATE WITH HIM')
print('HE SAID HE WILL GIVE YOU HINTS ON THE C00RDINATES')
print('PLEASE SAVE YOUR C0UNTRY')
print('OR ELSE ITS REPUTATI0N WILL BE RUINED')
print()
print('PRESS ENTER TO START\n')

min = 1
max = 30

x = random.randint(min, max)
y = random.randint(min, max)
coord = (x , y)

input()

attempts = 6
user_attempts = 0

done = False

while not done and user_attempts < attempts:
    n = (input('Guess the coordinates from 1 , 30 in the layout __,__ \n'))

    user_attempts = user_attempts + 1    

    x_guess , y_guess = map(int, n.split(','))

    if x_guess > x :
        print('x is smaller')
        attempts + 1

    if x_guess < x :
        print('x is larger')
        attempts + 1

    if y > y_guess :
        print('y is larger')
        attempts + 1

    if y_guess > y :
        print('y is smaller')
        attempts + 1

    if x_guess == x :
        print('x is correct')
        attempts + 1

    if y_guess == y :
        print('y is correct')
        attempts + 1

    if y_guess == y and x_guess == x :
        print('YOU FOUND IT')
        print('YOU HAVE DEACTIVATED YOUR B0MB AND SAVED', user_population, 'PE0PLE!')
        done = True

    if user_attempts == attempts and not done:
        print('BOOM!')
        print('BOOM!')
        print('BO0M!')
        print()
        print(' Y0U JUST EXPL0DED', user_population, 'PE0PLE')
        print(user_country, 'HAS BEEN EXPLODED BY', enemy)