def find_words(text, word):
    text_lower = text.lower()
    word_lower = word.lower()
    
    positions = []
    
    start = 0
    while True:
        start = text_lower.find(word_lower, start)
        if start == -1:
            break
        positions.append(start)
        start += len(word_lower)  # Продолжаем поиск с конца найденного слова

    return positions


text = open('./text.txt', 'r', encoding='utf8').read()
word = "по"  # 112
word = "по-"  # 1
word = " по "  # 9
positions = find_words(text, word)
print(f"Слово '{word}' найдено на позициях: {len(positions)}")
