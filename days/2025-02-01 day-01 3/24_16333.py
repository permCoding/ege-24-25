s = open('./24_16333.txt').readline()
s = s.replace('Q','W').replace('R','W')
s = s.replace('4','1').replace('2','1')

##s = '1111111WW1111111W11111W11W111W1111W1111111WW1111111111111111W111111W11111W11111111W1111111W1111111111111111111111W1W1W11W11'

mx = 1
sub = s[0]
for ch in s[1:]:
    sub += ch
    if sub[-2]+sub[-1] in ['11','WW']:
        sub = ch
    else:
        if len(sub) > mx:
            mx = len(sub)
print(mx)  # 17

'''
replace
strip
split

файл состоит из букв Q, R, W и цифр 1, 2, 4
Определите максимальное количество идущих подряд символов,
среди которых ни одна буква не стоит рядом с буквой, а цифра – с цифрой

Q11
22
44

'''
