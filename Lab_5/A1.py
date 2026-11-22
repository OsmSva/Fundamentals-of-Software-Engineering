import re

def delete_useless_symbols(text):
    while True:
        text, count = re.subn(r'\([^()]*\)', '', text)
        if count == 0:
            break
    return text

text = input("Введите строку: ")
print(delete_useless_symbols(text))
