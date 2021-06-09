from sys import exit

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
    """Insert the text snippet to the stage string"""
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


def print_stage(current_answer_list, letter_list, current_stage_number) -> None:
    def letter_to_text(letter):
        if letter:
            return " "+letter+" "
        return "   "

    try:
        with open("stage{0}.txt".format(current_stage_number), 'r') as f:
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
        # Used Letter
        ("Used letter:", 7, 1)
    ]
    letter_line_index = 8
    for letter_line in create_letter_list_for_print(letter_list).splitlines():
        text_snippet_list.append((letter_line, letter_line_index, 1))
        letter_line_index += 1
    print(insert_texts_into_stage(stage, text_snippet_list))


def main():
    print_stage(['A', None, 'B'], ['a', 'b', 'c',
                                   'd', 'f', 'f', 'g', 'g', 'f'], 9)


if __name__ == "__main__":
    main()
