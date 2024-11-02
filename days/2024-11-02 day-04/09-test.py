s = '5;5;45;45;5;45'
t = s.split(';')
nums = [int(e) for e in t]
##nums = list(map(int, t))
##nums = []
##for e in t:
##    nums.append(int(e))
np = []
nn = []
for e in nums:
    if nums.count(e) > 1:
        np.append(e)
    else:
        nn.append(e)
print(np, nn)

u1 = sum(1 for num in nums if nums.count(num)==3) == 3

u2 = sum(np) > sum(nn)

print(u1, u2)

##if u1 and u2:
##    k += 1

""" 6 чисел
– в строке только одно число повторяется трижды,
  остальные числа различны;
– квадрат суммы всех повторяющихся чисел строки
  больше квадрата суммы неповторяющихся чисел.
"""
