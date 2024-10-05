max_R = 0
for N in range(1, 13):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    max_R = max(int(b, 2), max_R)
print(max_R)





# b = ('10' + b) if N % 2 == 0 else ('1' + b + '01')


# s = '110'
# print(s + s)
# x = int(s, 10)
# print(x + x)







'''
s = '0123456'  # 7
print(s[0:])
print(s[0:4])
print(s[2:4])
print(s[0:len(s)])
print(s[0:7])
print(s[1:len(s)-1])
print(s[1:-1])
print(s[2:])
'''
