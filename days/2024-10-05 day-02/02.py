# проверка на чётность

n = 13

print('нечётное' if n % 2 > 0 else 'чётное')

d, m = divmod(n, 2)
##print(d, m)
print('нечётное' if m > 0 else 'чётное')

for n in range(1, 14):
    print(n, n & 1)

##
## 1100 = n = 12
## 0001 = 1
##-----
## 0000



'''
0110(2) =  6(10)
0101(2) =  5(10)
1111(2) = 15(10)
1100(2) = 12(10)


print(True and False)
print( (13 > 0) and (3 > 5) )

 a b and
 0 0  0
 0 1  0
 1 0  0
 1 1  1
'''
