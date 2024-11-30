from functools import reduce


def pr(nums):
    result = 1
    for num in nums:
        result *= num
    return result


t = [list(map(int, line.split(';'))) for line in open('./09.csv')]

amount = 0
for lst in t:
    evens = [e for e in lst if e%2==0]
    odds  = [e for e in lst if e%2!=0]
    if len(evens) >= 2 and len(odds) >= 2:
        # if 3*sum(odds) > pr(evens):
        if 3*sum(odds) > reduce(lambda a,b: a*b, evens, 1):
            amount += 1

print(amount)

"""
в строке не менее двух чётных и не менее двух нечётных чисел

утроенная сумма нечётных чисел больше произведения чётных
"""