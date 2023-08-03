import re

#Expressões regulares => re
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

#é número ou ponto
def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

#é número vazio
def isEmpty(string: str):
    return len(string) == 0