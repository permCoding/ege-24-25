def get(n):
    return sum(int(e) for e in list(str(abs(n))))
    
t = [int(e) for e in open('./17_18176.txt')]
mn = min(e for e in t if e>0 and e%10==4)

amount, lst = 0, []
for i in range(len(t)-2):
    sm = get(t[i]) + get(t[i+1]) + get(t[i+2])
    if sm == mn:
        amount += 1
        lst += [ t[i]+t[i+1]+t[i+2] ]
print(amount, max(lst))  # 11 180738

"""
Определите количество троек
сумма цифр элементов которых 
равна минимальному положительному элементу 
оканчивающемуся на 4
"""