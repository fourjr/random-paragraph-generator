import random


LIMIT = 200

with open('wordlist.txt') as f:
    words = f.read().splitlines()

random.shuffle(words)

words = words[:LIMIT]
semicolon = False

paragraph = ''
for n, i in enumerate(words):
    if n == 0 or paragraph[-2] in ('.', '!', '?'):
        paragraph += f'{i.capitalize()} '
    else:
        paragraph += f'{i} '

    semicolon_chance = 15 if semicolon else 30
    add_semicolon = not random.randint(0, semicolon_chance)
    add_punctuation = not random.randint(0, 10)
    add_comma = not random.randint(0, 5)
    if add_semicolon and paragraph[-2] != '"':
        if semicolon:
            paragraph = paragraph.strip()
            paragraph += '" '
            semicolon = False
        else:
            paragraph += '"'
            semicolon = True

    if add_comma:
        paragraph = paragraph.strip()
        paragraph += f', '

    PUNCTUATION = ('.', '!', '?', ',')
    if add_punctuation and paragraph[-2] not in PUNCTUATION:
        punc = random.choice(('.', '!', '?'))
        paragraph = paragraph.strip()
        paragraph += f'{punc} '

paragraph = paragraph[:-1] + '.'
print(paragraph)
