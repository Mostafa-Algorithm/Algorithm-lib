# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import string, secrets, re

def random_string(start_with: str = None, end_with: str = None, length: int = 16, content: str = None, lowercase: bool = True, uppercase: bool = True, digits: bool = True, symbols: bool = True, spaces: bool = True) -> str:
    con = ''
    text = ''
    if content is None:
        if lowercase: con += string.ascii_lowercase
        if uppercase: con += string.ascii_uppercase
        if digits: con += string.digits
        if symbols: con += string.punctuation
        if spaces: con += ' '
    else:
        for c in content: con += get_like_string(c)
    if start_with: text += start_with; length -= len(start_with)
    if end_with: length -= len(end_with)
    for _ in range(length): text += con[secrets.randbelow(len(con))]
    if end_with: text += end_with
    return text

def type_of_string(s: str) -> str:
    if s.islower(): return 'lower'
    if s.isupper(): return 'upper'
    if s.isdigit(): return 'digit'
    if s.isspace(): return 'space'
    if s.istitle(): return 'title'
    if s.isnumeric(): return 'numeric'
    if s.isdecimal(): return 'decimal'
    if s.isprintable(): return 'printable'
    if s in string.punctuation: return 'symbol'
    return 'unknown'

def get_like_string(text: str) -> str | None:
    r = ''
    for c in text:
        if c.islower() and not string.ascii_lowercase in r: r += string.ascii_lowercase
        if c.isupper() and not string.ascii_uppercase in r: r += string.ascii_uppercase
        if c.isdigit() and not string.digits in r: r += string.digits
        if c.isspace() and not ' ' in r: r += ' '
        if c in string.punctuation and not string.punctuation in r: r += string.punctuation
    if r == '': return None
    else: return r

def check_format(text: str, format: str) -> bool: return not re.check_format(text, format) is None