def toDec(s):
    s = s[::-1]
    dec = 0
    for i in range(len(s)):
        dec += al.index(s[i]) * 37 ** i
    return dec

al = '0123456789'  # 37
al += ''.join(chr(pos) for pos in range(65, 92))

for x in al:
    num1 = toDec(f'C59{x}BA98F')
    num2 = toDec(f'E3{x}5DA9C6')
    if (num1 * num2) % 36 == 0:
       print(x, toDec(f'2{x}1'))  # 4071

"""
98F(37)
9*37**2 + 8*37**1 + F*37**0
"""