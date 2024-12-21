import os
os.system('cls')

usr_wrd = input('Please input word:')
while not usr_wrd.isalpha():
    usr_wrd = input('Please input only alphabets. Please input word again :')

dec_enc = input('Do you want to decrypt or encrypt? 1:encrypt 0:decrypt :')
while dec_enc not in ['1','0']:
    dec_enc = input('Please input only 1 or 0. Please input again :')

offs = input('Please input offset?')
while not offs.isnumeric():
    offs = input('Please input only number Please input again :')
offs = int(offs)

ini_lst = []
for ltr in usr_wrd:
    base_alp = ord('a') if ltr.islower() else ord('A')
    modulo = offs % 26  # Wrap around after 26 letters
    
    if dec_enc == '1':  # Encrypt
        new_char = chr(base_alp + (ord(ltr) - base_alp + modulo) % 26)
    else:  # Decrypt
        new_char = chr(base_alp + (ord(ltr) - base_alp - modulo) % 26)
    ini_lst.append(new_char)

print(''.join(ini_lst))
    
        