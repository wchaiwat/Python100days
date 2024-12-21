import os
os.system('cls')

f_num = input('Please input first number :')
while not f_num.isnumeric():
    f_num = input('Thats incorrect, please input first number :')

oper = input('Please input operator + - * / :')
while oper not in ['+','-','*','/'] and len(oper) != 1:
    oper = input('Please input correct operator, please input again :')
    
    
s_num = input('Please input second number :')
while not s_num.isnumeric():
    s_num = input('Thats incorrect, please input second number :')
    

f_num = float(f_num)
s_num = float(s_num)

def calculator(f_num, s_num, oper):
    if oper == '+':
        return print(f'Result is {f_num + s_num}')
    elif oper == '-':
        return print(f'Result is {f_num - s_num}')
    elif oper == '*':
        return print(f'Result is {f_num * s_num}')
    else:
        if s_num == 0:
            return print(f'Result is : invalid, zero divisor')
        else:
            return print(f'Result is {f_num / s_num}')
    

calculator(f_num=f_num, s_num=s_num, oper=oper)