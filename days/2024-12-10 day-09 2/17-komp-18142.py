t = [int(e) for e in open('./17_18142.txt')]
mn = min(e for e in t if e%10==8)

amount = 0
pairs = []
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    if (a%16 == mn) ^ (b%16 == mn) == True:
        amount += 1
        pairs += [a+b]
print(amount, max(pairs))  # 1172 176024

"""
1
минимальному элементу последовательности, 
который оканчивается на 8
2
количество пар последовательности, 
в которых остаток от деления 
только одного из элементов на 16 
равен минимальному

a = False
b = True
print(a ^ b)
"""