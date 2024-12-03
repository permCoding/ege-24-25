import re


text = open('./text.txt', 'r', encoding='utf8').read()
# word = "по"  # 112
# word = "по-"  # 1
word = " по "  # 9

pattern = re.compile(word, re.IGNORECASE)
matches = pattern.findall(text)

print(f"Слово '{word}' найдено на позициях: {len(matches)}")

for m in matches: print(m)

"""
re.escape(word) - это можно использовать, если:
требуется экранировать символы, которые могут иметь 
специальное значение в регулярных выражениях, 
чтобы избежать ошибок при поиске
"""