import polars as pl 
import numpy as np
import os

os.system('cls')
files = pl.read_csv('Quiz\quiz_file_utf8.csv')

quest_dict = {}
for idx,row in enumerate(files.rows()):
    quest_dict[f'question_{idx}'] = {
        'quest':row[0],'a':row[1],'b':row[2],'c':row[3],'d':row[4],'ans':row[5]
    }
    
class QuizMultipleChoice:
    def __init__(self,quest_dict):
        self.quest_dict = quest_dict
        self.cur_score = 0
        self.cur_quest = 0
        self.quest_list = list(quest_dict.keys()) 
        
    def update_score(self,result):
        self.cur_quest += 1
        if result:
            return (self.cur_quest,self.cur_score+1)
        return (self.cur_quest,self.cur_score)
        
    def game_on(self):
        os.system('cls')
        quest_key = np.random.choice(self.quest_list)
        self.quest_list = [x for x in self.quest_list if x != quest_key]        
        
        print(f'Your score is now {self.cur_score} You have answered {self.cur_quest} question(s)')
        print(self.quest_dict[quest_key]['quest'])
        print(self.quest_dict[quest_key]['a'])
        print(self.quest_dict[quest_key]['b'])
        print(self.quest_dict[quest_key]['c'])
        print(self.quest_dict[quest_key]['d'])
        
        user_choice = input('Please choose answer :')
        while user_choice not in ['a','b','c','d']:
            user_choice = input('Invalid, Please choose answer :')
        
        if user_choice == self.quest_dict[quest_key]['ans']:
            (self.cur_quest,self.cur_score) = self.update_score(result=True)
        else:
            (self.cur_quest,self.cur_score) = self.update_score(result=False)
        
        print(f'answer was {self.quest_dict[quest_key]["ans"]}')
        print(f'Your score is now {self.cur_score} You have answered {self.cur_quest} question(s)')
        
        continue_play = input('Do you want to keep playing? 1:yes 0:no : ')
        while continue_play not in ['1','0']:
            continue_play = input('Invalid, Do you want to keep playing? 1:yes 0:no : ')
        
        if continue_play == '1':
            self.game_on()
        else:
            os.system('cls')
            print(f'Thank you for playing, You have total score {self.cur_score} from total {self.cur_quest} question(s)')
            
            
        
start_game = QuizMultipleChoice(quest_dict)
start_game.game_on()

    
