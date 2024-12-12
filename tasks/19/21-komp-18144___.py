def get(count): return [count-4, count-6, (count+1)//2]

S = 60
level0 = [S]

level1 = get(level0.pop())  # level 1 ходы ПЕТИ
if min(level1) > 19:  # Петя не должен выиграть
    print(S, level1)

    level2 = [get(count) for count in level1]  # level 2 ходы ВАНИ
    for elm in level2:
        if min(elm)<=19:  # ВАНЯ может выиграть своим 1-м ходом
            print(S, '+', elm)
        else:
            print(S, '-', elm)  # тут ВАНЯ НЕ выиграл первым ходом
        
