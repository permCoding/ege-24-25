# 1 - циклом по 9-чной СС
def get(dec):
    if dec == 0: return '0'
    res = ''
    while dec > 0:
        res = str(dec % 9) + res
        dec //= 9
    return res

cnt = 0
z = ['10','30','50','70','90','09','07','05','03','01']
for dec in range(0, int('88888', 9)+1):
    s = get(dec)
    if len(s) == 5 and s.count('0') == 1:
        if all((test not in s) for test in z):
            cnt += 1
print(cnt)
