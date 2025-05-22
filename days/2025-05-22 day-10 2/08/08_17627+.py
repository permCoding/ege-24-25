amount = 0
for n in range(2**32):
    e = hex(n)[2:].upper()
    if len(e) > 5: break
    if e[0] != '0' and len(e) == 5 and e.count('F') == 0:
        if e.count('8') == 1:
            if sum(1 for i in e if i in 'ABCDE') >= 2:
                amount += 1

print(amount)  # 83175

# hex(n)[2:]
# e.count('F') == 0