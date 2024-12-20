HANGMAN_STATES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]
import os
import wonderwords



def startgame():
    wrd = wonderwords.random_word.RandomWord().random_words(word_max_length=5)[0]
    wrd_list = [x for x in wrd]
    init_state = ['_' for x in range(len(wrd_list))]
    st = 0
    record_list = []
    while st <= len(HANGMAN_STATES)-1:
        os.system('cls')
        print(HANGMAN_STATES[st])
        print(init_state)
        
        if st == len(HANGMAN_STATES)-1:
            print('You lose')
            print(f'The word is {wrd}')
            break
        elif st < len(HANGMAN_STATES)-1 and '_' not in init_state:
            print('You win')
            print(f'The word is {wrd}')
            break
        else:
            usr = input('Please guess a letter :')
            while not usr.isalpha() or len(usr) != 1 or usr in record_list:
                print('Invalid')
                usr = input('Please guess a letter again (only one letter and not the previous one):')
            
            record_list.append(usr)
            if usr in wrd_list:
                for idx, ele in enumerate(wrd_list):
                    if ele == usr:
                        init_state[idx] = ele
            else:
                st += 1 

Wannaplaygain = '1'
while Wannaplaygain == '1':
    startgame()
    Wannaplaygain = input('Wanna play again? 1:yes 0:no :')
    while Wannaplaygain not in ['1', '0']:
        Wannaplaygain = input('INVALID--- Wanna play again? 1:yes 0:no :')
    