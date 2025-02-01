s = open('./24_16333.txt') \
    .readline() \
    .replace('Q','W') \
    .replace('R','W') \
    .replace('4','1') \
    .replace('2','1')

mx = 1
sub = s[0]
for ch in s[1:]:
    sub += ch
    if sub[-2:] in ['11','WW']:
        sub = ch
    else:
        mx = max(mx, len(sub))
print(mx)  # 17

'''
файл состоит из букв Q, R, W и цифр 1, 2, 4
Определите максимальное количество идущих подряд символов,
среди которых ни одна буква не стоит рядом с буквой, а цифра – с цифрой
'''
