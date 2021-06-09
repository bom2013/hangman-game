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


for i in range(13):
    with open("stage"+str(i)+".txt", 'r') as f:
        print(f.read())
