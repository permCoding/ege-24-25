k = 0
for line in open('./09-18258.csv'):
    k += 1
    t = [int(e) for e in line.split(';')]
    srt = sorted(t)
    if ''.join(map(str, t)) == ''.join(map(str, srt)):
        p = [e for e in t if t.count(e) > 1]
        if len(p) > 0:
            if any(sum(map(int, list(str(e)))) %2 == 0 for e in p):
                print(k, t)  # 6937

"""
пределите наибольший номер строки таблицы,
для чисел которой выполнены оба условия:
– числа в строке расположены в порядке неубывания;
– в строке есть повторяющиеся числа с чётной суммой цифр.
"""
