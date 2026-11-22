words = input("Введите слова через пробел: ").split()

result = ""
for word in words:
    if len(word) > 2:
        result += word[0].upper()
print(f"Аббревиатура: {result}")
