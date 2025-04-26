from itertools import product as p

amount, al = 0, 'АИЭДГШ'
for combo in p(al, repeat=5):
    if combo[0] in al[3:] and combo[-1] in al[:3]:
        amount += 1

print(amount)  # 1944
