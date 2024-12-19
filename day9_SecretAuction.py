import os
def clear_screen():
    # Clear the console screen
    os.system('cls||clear')

what_to_auc = input('input action stuff :')
how_much = input('input start price :')
while not how_much.isdigit():
    print('Please input only number...')
    how_much = input('input start price :')
how_much = float(how_much)


continue_yesno = 1
names = []
price_list = []
current_price = 0

while continue_yesno == 1:
    who = input('what is your name :')
    how_much_to_auc = input('how much you want to auction :')
    
    while not how_much_to_auc.isdigit():
        print('Please input only number...')
        how_much_to_auc = input('how much you want to auction :')
    
    how_much_to_auc = float(how_much_to_auc)
    
    
    if how_much_to_auc >= current_price:
        current_price = how_much_to_auc


    price_list.append(how_much_to_auc)
    names.append(who)
    continue_yesno = input('Is there anyone else want to auction? 1:yes 0:no ')
    
    while continue_yesno not in ['1','0']:
        print('please input only 1 or 0')
        continue_yesno = input('Is there anyone else want to auction? 1:yes 0:no ')
    
    clear_screen()

winner_price = max(price_list)
counter = 0
for idx, pr in enumerate(price_list):
    if winner_price == pr:
        counter += 1

if counter == 1:
    winner_name = [names[idx] for idx, y in enumerate(price_list) if winner_price == y][0]
    print(f'{winner_name} is the person who win the auction with price {winner_price}')
else:
    winner_name = [names[idx] for idx, y in enumerate(price_list) if winner_price == y]
    print(f'{winner_name} are the persons who win the auction with price {winner_price}')


