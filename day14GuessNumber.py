import os
import numpy as np

def still_wanna_play():
    user_choice = input('Do you still wanna play? 1:yes 0:no :')
    while user_choice not in ['1','0']:
        user_choice = input('Invalid, Do you still wanna play? 1:yes 0:no :')
    if user_choice == '1':
        game_on()
    else:
        exit()

def game_on():
    os.system('clear')
    print('Welcom to guessing number game')

    game_level = input('Please select difficulty 0:easy 1:intermediate 2:hard :')
    while game_level not in ['0','1','2']:
        game_level = input('Invalid, Please select difficulty 0:easy 1:intermediate 2:hard :')

    rounds = {'0':10, '1':7, '2':5}
    cnt = 0

    rand_num = np.random.randint(low=0, high=1001)

    while cnt<rounds[game_level]:
        usr_guess = input('Please guess the number :')
        
        while not usr_guess.isnumeric() or int(usr_guess) > 1000 or int(usr_guess) < 0:
            if usr_guess.isnumeric():
                usr_guess = input('Invalid, Please guess the number :')
            else:
                usr_guess = input('Invalid, Please guess the number between 0-1000 :')

        if int(usr_guess) < rand_num:
            print(f'Too low, Please guess higher !, You have guessd {cnt+1}/{rounds[game_level]}')
        elif int(usr_guess) > rand_num:
            print(f'Too high, Please guess lower !! You have guess {cnt+1}/{rounds[game_level]}')
        else:
            print('You got it right !!')
            still_wanna_play()

        cnt += 1
    print(f"You've run out of tries, the number was {rand_num}")
    still_wanna_play()

game_on()




        