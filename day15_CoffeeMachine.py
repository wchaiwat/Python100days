import os
import numpy as np

os.system('cls')

coffee_dict = {'espresso':{
    'ingredients':{'water':50, 'milk':0, 'coffee':18},
    'cost':1.5
        },
    'latte':{
        'ingredients':{'water':200, 'milk':150, 'coffee':24},
        'cost':2.5
        },
    'cappuccino':{
        'ingredients':{'water':250, 'milk':100, 'coffee':24},
        'cost':3.0
        },
    'macciato':{
        'ingredients':{'water':100, 'milk':50, 'coffee':12},
        'cost':2.0
        },
    'americano':{
        'ingredients':{'water':300, 'milk':0, 'coffee':30},
        'cost':2.5
        }
    }

with open(r'C:\Users\wchaiwat\Documents\VSProject\python100days\day_14_folder\day14_CoffeeMachine.txt','w') as file:
    water = 1000
    milk = 500
    coffee = 200
    
    file.writelines(f'water:{water}\n')
    file.writelines(f'milk:{milk}\n')
    file.writelines(f'coffee:{coffee}\n')
       
   

def refill_ingredients():
    with open(r'C:\Users\wchaiwat\Documents\VSProject\python100days\day_14_folder\day14_CoffeeMachine.txt', 'w') as file:
        add_water = input('How much water you want to add :')
        add_milk = input('How much milk you want to add :')
        add_coffee = input('How much coffee you want to add :')
        while not add_water.isnumeric() or not add_milk.isnumeric() or not add_coffee.isnumeric():
            add_water = input('Invalid, How much water you want to add :')
            add_milk = input('Invalid, How much milk you want to add :')
            add_coffee = input('Invalid, How much coffee you want to add :')
        file.write(f'water:{water + int(add_water)}\n')
        file.write(f'milk:{milk + int(add_milk)}\n')
        file.write(f'coffee:{coffee + int(add_coffee)}\n')
        print('Ingredients refilled successfully!!')
        
def check_ingredients(user_choice):
    with open(r'C:\Users\wchaiwat\Documents\VSProject\python100days\day_14_folder\day14_CoffeeMachine.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('water'):
                water = int(line.split(':')[1])
            elif line.startswith('milk'):
                milk = int(line.split(':')[1])
            elif line.startswith('coffee'):
                coffee = int(line.split(':')[1])
                
        if water < coffee_dict[list(coffee_dict.keys())[int(user_choice)]]['ingredients']['water']:
            print('Sorry, there is not enough water')
            have_you_finished()
        elif milk < coffee_dict[list(coffee_dict.keys())[int(user_choice)]]['ingredients']['milk']:
            print('Sorry, there is not enough milk')
            have_you_finished()
        elif coffee < coffee_dict[list(coffee_dict.keys())[int(user_choice)]]['ingredients']['coffee']:
            print('Sorry, there is not enough coffee')
            have_you_finished()
        else:
            print('Please wait, making coffee....')
            return True
    

print('Welcome to Coffee Machine')

def start_coffee_machine():
    os.system('cls')
    user_action = input('What would you like to do? 0:Report, 1:Refill, 2:Order coffee :')
    while user_action not in ['0','1','2']:
        user_action = input('Invalid, What would you like to do? 0:Report, 1:Refill, 2:Order coffee :')
        
        
    if user_action == '0':
        print(f'Water : {water}\nMilk : {milk}\nCoffee : {coffee}')
        have_you_finished()
    elif user_action == '1':
        refill_ingredients()
        have_you_finished()
    else:
        user_choice = input('0:espresso, 1:latte, 2:cappuccino, 3:macciato, 4:americano :')
        while user_choice not in ['0','1','2','3','4']:
            user_choice = input('Invalid, Please select your coffee :')
            
        print(f'You have selected {list(coffee_dict.keys())[int(user_choice)]} coffee')
        print(f'Cost of coffee is {coffee_dict[list(coffee_dict.keys())[int(user_choice)]]["cost"]}')

        
        check_ingredients(user_choice=user_choice)
        
        
        print('Please insert coins')
        user_dime = input('How many dimes :')
        user_nickel = input('How many nickels :')
        user_quarter = input('How many quarters :')
        user_penny = input('How many pennies :')

        while not user_dime.isnumeric() or not user_nickel.isnumeric() or not user_quarter.isnumeric() or not user_penny.isnumeric():
            user_dime = input('Invalid, How many dimes :')
            user_nickel = input('Invalid, How many nickels :')
            user_quarter = input('Invalid, How many quarters :')
            user_penny = input('Invalid, How many pennies :')
        
        total_money = int(user_dime)*0.1 + int(user_nickel)*0.05 + int(user_quarter)*0.25 + int(user_penny)*0.01
        print(f'Total money inserted is ${total_money}')

        if total_money < coffee_dict[list(coffee_dict.keys())[int(user_choice)]]['cost']:
            print('Insufficient money, Money refunded')
            have_you_finished()
        else:
            with open(r'C:\Users\wchaiwat\Documents\VSProject\python100days\day_14_folder\day14_CoffeeMachine.txt','w') as file:
                file.write(f'water:{water - coffee_dict[list(coffee_dict.keys())[int(user_choice)]]["ingredients"]["water"]}\n')
                file.write(f'milk:{milk - coffee_dict[list(coffee_dict.keys())[int(user_choice)]]["ingredients"]["milk"]}\n')
                file.write(f'coffee:{coffee - coffee_dict[list(coffee_dict.keys())[int(user_choice)]]["ingredients"]["coffee"]}\n')


            print(f'Here is your {list(coffee_dict.keys())[int(user_choice)]} coffee. Enjoy!!')
            print(f'Here is your change ${total_money - coffee_dict[list(coffee_dict.keys())[int(user_choice)]]["cost"]}')
            have_you_finished()
            
def have_you_finished():
    user_action = input('Do you want to continue? y:Yes, n:No :')
    while user_action not in ['y','n']:
        user_action = input('Invalid, Do you want to continue? y:Yes, n:No :')
    
    if user_action == 'y':
        start_coffee_machine()
        have_you_finished()
    else:
        print('Goodbye!!')

start_coffee_machine()
        
        
    


    

        
