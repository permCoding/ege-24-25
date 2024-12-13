def get(count):
    return [count-3, count-5, count//2]

for S in range(18, 99):  # ищем минимальное

    level1 = get(S)  # level 1 ходы Пети
    if any(e<=17 for e in level1): continue # Петя не должен выиграть
    
    level2 = [get(count) for count in level1]
    
    if all(any(e<=17 for e in combo) for combo in level2):
        print(S)  # 36
        break
