import re

text = input("Введите текст: ")
sentences = re.split(r'(?<=[.?!]) ', text)
for sentence in sentences:
    print(sentence)
print(f"Предложений в тексте: {len(sentences)}")
