def get(count):
    return [count-4, count-6, (count+1)//2]

for S in range(20, 99):

    level1 = get(S)  # level 1 ходы Пети
    
    if min(level1) <= 19: continue  # Петя не должен выиграть
    
    level2 = [get(count) for count in level1]
    
    if all(min(combo)<=19 for combo in level2): break

print(S)
