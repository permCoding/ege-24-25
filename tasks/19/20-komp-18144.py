def get(count):
    return [count-4, count-6, (count+1)//2]

def check(combo):
    return (max(combo)+1)//2<=19

for S in range(20, 60):
    
    level1 = get(S)
    if min(level1) <= 19: continue  # Петя не должен выиграть
    
    level2 = [get(count) for count in level1]  # level 2 ВАНЯ
    print(S, level2)    
    if all(check(combo) for combo in level2):
        print(S)  # 43, 44
