import numpy
import os

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

class CoffeeMachine:
    def __init__(self,water,coffee,milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        
        with open('Coffee_report.txt', mode='w') as coffee_ref:
            coffee_ref.write(f"Water: {self.water} ml\n")
            coffee_ref.write(f"Coffee: {self.coffee} g\n")
            coffee_ref.write(f"Milk: {self.milk} ml\n")
    
    def user_action(self):
        
        while True:
            
            user_choice = input('What do you want to do? 0:Report, 1:BuyCoffee, 2:Refill, 3:Exit: ')
            while not user_choice.isdigit() or user_choice not in ['0', '1', '2', '3']:
                user_choice = input('Invalid choice. Try again: 0:Report, 1:BuyCoffee, 2:Refill, 3:Exit: ')

            if user_choice == '0':
                self.init_report()
            elif user_choice == '1':
                self.make_coffee()
            elif user_choice == '2':
                fill_water = input('How much water to refill?: ')
                fill_milk = input('How much milk to refill?: ')
                fill_coffee = input('How much coffee to refill?: ')

                # Validate refill inputs
                while not (fill_water.isdigit() and fill_milk.isdigit() and fill_coffee.isdigit()):
                    print('Invalid inputs. Please enter positive numbers.')
                    fill_water = input('How much water to refill?: ')
                    fill_milk = input('How much milk to refill?: ')
                    fill_coffee = input('How much coffee to refill?: ')

                self.refill(int(fill_water), int(fill_milk), int(fill_coffee))
            elif user_choice == '3':
                print("Goodbye!")
                break

        
        
    def init_report(self):
        
        with open('Coffee_report.txt', mode='w') as coffee_ref:
            coffee_ref.write(f"Water: {self.water} ml\n")
            coffee_ref.write(f"Coffee: {self.coffee} g\n")
            coffee_ref.write(f"Milk: {self.milk} ml\n")
        
        return print(f'Current Stock >> \n Water {self.water} ml \n Coffee {self.coffee} g \n Milk {self.milk} ml')
    
    def check_sufficient_resource(self,coffee_name,total_insert):
        
        with open('Coffee_report.txt', mode='r') as coffee_ref:
            lines = coffee_ref.readlines()
            for line in lines:
                if line.startswith('Water'):
                    self.water = int(line.split(':')[1].strip().split()[0])
                elif line.startswith('Milk'):
                    self.milk = int(line.split(':')[1].strip().split()[0])
                elif line.startswith('Coffee'):
                    self.coffee = int(line.split(':')[1].strip().split()[0])
        
        if self.water<coffee_dict[coffee_name]['ingredients']['water']:
            print('Water not enough')
            print(f'Money refunded {total_insert}')
            return False
        elif self.milk<coffee_dict[coffee_name]['ingredients']['milk']:
            print('Milk not enough')
            print(f'Money refunded {total_insert}')
            return False
        elif self.coffee<coffee_dict[coffee_name]['ingredients']['coffee']:
            print('coffee not enough')
            print(f'Money refunded {total_insert}')
            return False
        
        return True
    
    def refill(self, fill_water, fill_milk, fill_coffee):
        self.water += fill_water
        self.milk += fill_milk
        self.coffee += fill_coffee
        self.init_report()  # Write updated values to the file
        print("Machine refilled successfully!")

    
    def update_resource(self, coffee_name):
        self.water -= coffee_dict[coffee_name]['ingredients']['water']
        self.milk -= coffee_dict[coffee_name]['ingredients']['milk']
        self.coffee -= coffee_dict[coffee_name]['ingredients']['coffee']
        self.init_report()  # Update the file with the new values


    
    
    def make_coffee(self):
        coffee_choice_number = input('what_coffee_do_you_want_buy 0:espresso, 1:latte, 2:cappuccino, 3:macciato, 4:americano')
        while not coffee_choice_number.isnumeric():
            coffee_choice_number = input('Invalid, what_coffee_do_you_want_buy 0:espresso, 1:latte, 2:cappuccino, 3:macciato, 4:americano')
        
        coffee_idx = {idx:cf for idx, cf in enumerate(coffee_dict.keys())}
        

        print(f"{coffee_idx[int(coffee_choice_number)]} cost : {coffee_dict[coffee_idx[int(coffee_choice_number)]]['cost']}")
        print('Please insert coins')
        
        pennies = input('How many pennies : ')
        nickels = input('How many nickels : ')
        dimes = input('How many dimes : ')
        quarters = input('How many quarters : ')
        
        while True:
            pennies = input('How many pennies : ')
            if not pennies.isnumeric():
                continue
            nickels = input('How many nickels : ')
            if not nickels.isnumeric():
                continue
            dimes = input('How many dimes : ')
            if not dimes.isnumeric():
                continue
            quarters = input('How many quarters : ')
            if not quarters.isnumeric():
                continue
            break
        
        total_insert = int(pennies)*1 + int(nickels)*5 + int(dimes)*10 + int(quarters)*25
        
        while total_insert < coffee_dict[coffee_idx[int(coffee_choice_number)]]['cost']:
            print('The total money is less than the coffee price, Please insert more coins!')
            pennies = input('How many pennies : ')
            nickels = input('How many nickels : ')
            dimes = input('How many dimes : ')
            quarters = input('How many quarters : ')
            
            while True:
                pennies = input('How many pennies : ')
                if not pennies.isnumeric():
                    continue
                nickels = input('How many nickels : ')
                if not nickels.isnumeric():
                    continue
                dimes = input('How many dimes : ')
                if not dimes.isnumeric():
                    continue
                quarters = input('How many quarters : ')
                if not quarters.isnumeric():
                    continue
                break
              
        if self.check_sufficient_resource(coffee_idx[int(coffee_choice_number)], total_insert):
            print('Here is your coffee, ENJOY!')
            self.update_resource(coffee_idx[int(coffee_choice_number)])
            if total_insert == coffee_dict[coffee_idx[int(coffee_choice_number)]]['cost']:
                self.user_action()
            else:
                print(f"Here is your change {total_insert - coffee_dict[coffee_idx[int(coffee_choice_number)]]['cost']}")
                self.user_action()
        else:
            self.user_action()
                

my_coffee = CoffeeMachine(1000,1000,1000)
my_coffee.user_action()