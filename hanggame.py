# Auther: Noam Ben Shlomo(bom2013)
from sys import exit
import random
import time
import os

# Seed random
random.seed(time.time())

# Set level entry point
START_POINT0 = 0
START_POINT1 = 3


def get_extended_stage(stage_string, text_snippet_list) -> str:
    """Extend the stage_string according to the size required from text_snippet_list"""
    max_shift = max([(len(text_snippet[0])+text_snippet[2])
                     for text_snippet in text_snippet_list])
    extended_stage = ''
    for line in stage_string.splitlines():
        extended_stage += ' '*max_shift + line + '\n'
    return extended_stage


def add_text_snippet(stage_string, text_snippet) -> str:
    """Insert the text snippet to string"""
    text, line, offset = text_snippet
    text_lines = stage_string.splitlines()
    changed_line = text_lines[line]
    changed_line = changed_line[:offset] + \
        text + changed_line[len(text)+offset:]
    text_lines[line] = changed_line
    return "\n".join(text_lines)


def insert_texts_into_stage(stage_string, text_snippet_list) -> str:
    """Insert texts into stage string"""
    extended_stage = get_extended_stage(stage_string, text_snippet_list)
    for text_snippet in text_snippet_list:
        extended_stage = add_text_snippet(extended_stage, text_snippet)
    return extended_stage


def create_letter_list_for_print(letter_list) -> str:
    """Create letter string for printing"""
    res = ""
    for i in range(len(letter_list)):
        if not i % 5 and i:
            res += '\n'
        res += letter_list[i]+" "
    return res


def print_stage(current_answer_list, letter_list, current_stage_number, number_of_guess) -> None:
    '''Print stage to screen'''
    def letter_to_text(letter):
        if letter:
            return " "+letter+" "
        return "   "

    try:
        with open("files\\stage{0}.txt".format(current_stage_number), 'r') as f:
            stage = f.read()
    except Exception:
        print("Error! could not open stage file number", current_stage_number)
        exit(-1)

    text_snippet_list = [
        # Answer letter
        (" ".join([letter_to_text(letter)
                   for letter in current_answer_list]), 3, 1),
        # lines
        (" ".join(['---' for i in range(len(current_answer_list))]), 4, 1),
        # Number of guess
        ("Number of guess: "+str(current_stage_number), 6, 1),
        # Number of guess left
        ("Number of guess left: "+str(13-current_stage_number), 7, 1),
        # Used Letter
        ("Used letter:", 8, 1)
    ]
    letter_line_index = 9
    for letter_line in create_letter_list_for_print(letter_list).splitlines():
        text_snippet_list.append((letter_line, letter_line_index, 1))
        letter_line_index += 1
    print(insert_texts_into_stage(stage, text_snippet_list))


def print_win_message():
    '''Print win message using win.txt'''
    try:
        with open("files\\win.txt", 'r') as f:
            print(f.read())
    except Exception:
        print("Error! could not open win file")
        exit(-1)


def get_word() -> str:
    '''Get random word from words.txt'''
    with open('files\\words.txt') as f:
        words_list = f.readlines()
    word_index = random.randint(0, len(words_list)-1)
    return words_list[word_index][:-1]


def check_is_win(word, letter_list) -> bool:
    '''Check if guess all letter in word'''
    for letter in word:
        if letter not in letter_list:
            return False
    return True


def create_printable_mask_list(word, letter_list) -> list:
    '''Create printable mask of word for printing
    \nExample:
    \n\tword = 'hello', letters = ['l','h']
    \n=> ['h', None, 'l', 'l', None]
    '''
    mask = []
    for letter in word:
        if letter in letter_list:
            mask.append(letter)
        else:
            mask.append(None)
    return mask


def clear_screen() -> None:
    '''Clear screen'''
    if os.name == 'posix':  # linux\mac
        os.system('clear')
    else:  # window
        os.system('cls')


def print_loss_message() -> None:
    '''Print loss message using loss.txt'''
    try:
        with open("files\\loss.txt", 'r') as f:
            print(f.read())
    except Exception:
        print("Error! could not open loss file")
        exit(-1)


def play(start_level):
    '''Handle the game'''
    word = get_word()
    letter_used = []
    number_of_step = 0
    current_level = start_level
    while True:
        clear_screen()
        # Check if user guess all word
        if check_is_win(word, letter_used):
            print_win_message()
            exit()
        # Check if reach all levels
        elif current_level > 12:
            print_loss_message()
            exit()
        else:
            print_stage(create_printable_mask_list(word, letter_used),
                        letter_used,
                        current_level,
                        number_of_step)
            new_letter = input("Enter letter: ")[0]
            if new_letter in word:
                if new_letter in letter_used:
                    print("You already used this letter")
                else:
                    print("Nice guess!")
            else:
                print("Wrong guess! I'm getting closer to hanging ...")
                current_level += 1
            letter_used.append(new_letter)
            number_of_step += 1
            time.sleep(0.6)


def main():
    while True:
        print("-"*10)
        print("1. easy")
        print("2. hard")
        print("*. exit")
        res = input()
        if res not in '12':
            exit()
        play(START_POINT0 if res == '1' else START_POINT1)


if __name__ == "__main__":
    main()
