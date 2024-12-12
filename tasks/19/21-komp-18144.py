def get(count): return [count-4, count-6, (count+1)//2]

for S in range(99, 19, -1):  # ищем максимальное
    
    # level 0
    level0 = [S]
    
    # level 1 ПЕТЯ
    level1 = get(level0.pop())  # ходы ПЕТИ
    if min(level1) <= 19: continue  # Петя не должен выиграть
    print(S, level1)
    # level 2 ВАНЯ
    level2 = [get(count) for count in level1]  # ходы ВАНИ
    res = [min(elm)<=19 for elm in level2]
    if any(res): print(S, level2)  # первым ходом ВАНИ
        
