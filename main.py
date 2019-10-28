import math
import random
import string
import sys
import pyperclip

try:
    LIMIT = int(sys.argv[1])
except IndexError:
    LIMIT = 200
except ValueError as e:
    raise RuntimeError('invalid number') from e

with open('wordlist.txt', encoding='utf8') as f:
    words = f.read().splitlines()

for i in words:
    if any(j in i for j in string.digits):
        words.remove(i)

words *= math.ceil(LIMIT / len(words))
random.shuffle(words)

words = words[:LIMIT]

for i in words:
    if len(i) > 1:
        LIMIT -= 1

random.shuffle(words)
words = words[:LIMIT]

semicolon = False

paragraph = ''
for n, i in enumerate(words):
    if n == 0 or paragraph[-2] in ('.', '!', '?'):
        paragraph += f'{i.capitalize()} '
    else:
        paragraph += f'{i} '

    semicolon_chance = 9 if semicolon else 30
    add_semicolon = not random.randint(0, semicolon_chance)
    add_punctuation = not random.randint(0, 7)
    add_comma = not random.randint(0, 7)
    if add_semicolon and paragraph[-2] != '"':
        if semicolon:
            paragraph = paragraph.rstrip()
            paragraph += '" '
            semicolon = False
        else:
            paragraph += '"'
            semicolon = True

    if add_comma and paragraph[-2] not in ('.', '!', '?', ',') and paragraph[-1] != '"':
        paragraph = paragraph.rstrip()
        paragraph += ', '

    if add_punctuation and paragraph[-2] not in ('.', '!', '?', ',') and paragraph[-1] != '"':
        punc = random.choice(('.', '!', '?'))
        paragraph = paragraph.rstrip()
        paragraph += f'{punc} '

if semicolon:
    if paragraph[-1] == '"':
        paragraph = paragraph[:-1]
    else:
        if paragraph[-2] in ('.', '!', '?', ','):
            paragraph = paragraph[:-2] + '"'
        else:
            paragraph = paragraph[:-1] + '"'

if len(paragraph) > 1 and paragraph[-2] in ('.', '!', '?', ','):
    paragraph = paragraph[:-2] + '.'
elif len(paragraph) > 0 and paragraph[-1] == '"':
    paragraph += '.'
elif len(paragraph) > 0:
    paragraph = paragraph[:-1] + '.'


print(paragraph)
