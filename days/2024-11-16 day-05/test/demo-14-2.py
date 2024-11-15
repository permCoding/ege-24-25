def get(n, base=25):
    r = ''
    while n > 0:
        o = n%base
        n //= base
        r = str(o) + r
    return r

n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 -2025
w = get(n)
print(w.count('0'), w)  # 9

    
# s = '0123456789'
# s += ''.join(chr(i) for i in range(65, 80))
# print(len(s), s)
# print(3*3125**8)
