import random

word_list = ['papu','pro','vaina','progra','charles']
MAX_FAILS = 3

def print_status_bar(strikes, word, correct):
    print_line()
    masked_word = mask_word(word, correct)
    strikes_string = '[X]'*strikes + '[ ]'* (MAX_FAILS-strikes)
    print('word', masked_word)
    print('strikes', strikes_string)
    print_line()

def mask_word(word, correct):
    return list(map(lambda c: c if c in correct else '_', list(word)))

def print_line():
    print("*"*32)

def select_word(list):
    return random.choice(list)

def do_game():
    fails = 0
    word = select_word(word_list)
    unique_characters = set(word)
    correct_characters = set()

    while(fails < MAX_FAILS):
        print_status_bar(fails, word, correct_characters)
        letter = input('enter a character:')
        print('your selected: ',letter)
        if(letter in unique_characters):
            unique_characters.remove(letter)
            correct_characters.add(letter)
            print('correct! =)')
            if(len(unique_characters) == 0):
                print_status_bar(fails, word, correct_characters)
                return True
        else:
            fails+= 1
            print('strike! =(: ')
    return False

def main():
    if do_game():
        print_line()
        print('you win ( ͡❛ ͜ʖ ͡❛)')
    else:
        print_line()
        print('you lose ( ͡⊙ ͜ʖ ͡⊙)')

if __name__ == '__main__':
    main()

