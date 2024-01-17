import random

MAX_FAILS = 5

def print_status_bar(strikes, word, correct):
    print_line()
    masked_word = mask_word(word, correct)
    strikes_string = create_strikes_board(strikes)
    print('word', masked_word)
    print('strikes', strikes_string)
    print_line()

def mask_word(word, correct):
    return list(map(lambda c: c if c in correct else '_', word))

def create_strikes_board(strikes):
    return '[X]'*strikes + '[ ]'* (MAX_FAILS-strikes)


def print_line():
    print("*"*32)

def select_word(list):
    return random.choice(list)

def do_game():
    strikes = 0
    word_list = load_list()
    word = select_word(word_list)
    unique_characters = set(word)
    correct_characters = set()

    while(strikes < MAX_FAILS):
        print_status_bar(strikes, word, correct_characters)
        letter = input('enter a character:')
        print('your selected: ',letter)
        if(letter in unique_characters):
            unique_characters.remove(letter)
            correct_characters.add(letter)
            print('correct! =)')
            if(len(unique_characters) == 0):
                print_status_bar(strikes, word, correct_characters)
                return True
        else:
            strikes+= 1
            print('strike! =(: ')
    return False

def main():
    if do_game():
        print_line()
        print('you win 😎')
    else:
        print_line()
        print('you lose 😭')

def load_list():
    file = open('./0_palabras_todas_no_conjugaciones.txt','r')
    return file.read().splitlines()


if __name__ == '__main__':
    main()

