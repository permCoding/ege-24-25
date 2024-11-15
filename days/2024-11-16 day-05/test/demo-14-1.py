s = '0123456789' + ''.join(chr(i) for i in range(65, 74))
for x in s:
    a = int(f'98897{x}21', 19)
    b = int(f'2{x}923', 19)
    r = a + b
    if r%18 == 0:
        print(x, r//18)  # F 469034148