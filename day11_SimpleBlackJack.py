import numpy as np
import os

def game_on():
    os.system('cls')


    def total_card_score(card_list, card_dict):
        sc = 0
        for card in card_list:
            sc += card_dict[card]
        return sc

    def result_win_lose(sc1,sc2):
        if sc1 > 21 and sc2 <= 21:
            return "User BUST!!!, Computer wins"
        elif sc2 > 21 and sc1 <= 21:
            return "User win, Computer BUST!!!"
        elif sc1 > 21 and sc2 > 21:
            return "Draw, Both BUST!!!"
        elif abs(21-sc1) < abs(21-sc2):
            return "User win"
        elif abs(21-sc1) == abs(21-sc2):
            return "Draw"
        else:
            return "Computer win"


    card_shape = ['Heart','Diamond','Spade','Club']
    card_unit = list(np.arange(start=1, stop=11)) + ['Jack','King', 'Queen']

    card_dict = {}
    counter = 1
    score = 0
    for cs in card_shape:
        for cu in card_unit:
            if cu in ['Jack','King', 'Queen']:
                score = 10
            else:
                score = cu
            
            card_dict[f'{cs}_{cu}'] = score
            
    card_list = list(card_dict.keys())
    user_card = np.random.choice(card_list,size=2)
    comp_card = np.random.choice([x for x in card_list if x not in user_card],size=2)


    print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 
          ''')
    print('Welcome to Blackjack game ----\n')
    print(f'Your 2 cards are {user_card} and first computer card is {comp_card[0]}')

    add_more = input('Do you want to add one more card?, 1:yes 0:no :')
    while add_more not in ['1','0']:
        add_more = input('Invalid, Please input only 1 or 0, Do you want to add one more card?, 1:yes 0:no :')

    if add_more == '1':
        add_card = np.random.choice([x for x in card_list if x not in list(user_card)+list(comp_card)], size=1)
        user_card = np.append(user_card, add_card)


    print(f'Your card are {user_card} and Both computer cards are {comp_card}')
    sc1 = total_card_score(card_list=user_card, card_dict=card_dict)
    sc2 = total_card_score(card_list=comp_card, card_dict=card_dict)
    print(f'Your total score is {sc1} and Computer score is {sc2}, {result_win_lose(sc1=sc1, sc2=sc2)}')
    
while True:
    game_on()
    user_cont = input('Do you want to continue?? 1:yes 0:no ')
    while user_cont not in ['1','0']:
        user_cont = input('Invalid!, Do you want to continue?? 1:yes 0:no ')

    if user_cont == '0':
        exit()
        