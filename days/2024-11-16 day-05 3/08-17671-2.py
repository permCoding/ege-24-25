##combo = ('Й', 'Й', 'А', 'Й', 'Й')
##print(''.join(combo))

# var 2
from itertools import product

for i, combo in enumerate(product('АЙЛМ', repeat=5), start=1):
    if combo.count('М')==0 and combo.count('Л')==0:
##        if ''.join(combo).find('ЙЙ') == -1:
        if 'ЙЙ' not in ''.join(combo):
            print(i, combo)

# var 3



"""
Все пятибуквенные слова, в составе которых могут быть
только русские буквы Л, А, Й, М, записаны в алфавитном
порядке и пронумерованы начиная с 1.

1. ААААА
2. ААААЙ
3. ААААЛ
4. ААААМ
5. АААЙА

Под каким номером в списке идёт последнее слово, которое
не содержит ни одной буквы М, ни одной буквы Л и
не содержит букв Й стоящих рядом?

0. 00000 А
1. 00001 Й
2. 00002 Л
3. 00003 М
4. 00010
5. 00011


X. 10101

"""
