lst = []
for n in range(1, 26):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = '10' + b + '1'
    else:
        b = '10' + b + '0111'
    r = int(b, 2)
    lst.append(r)  # 1415
print(max(lst))
