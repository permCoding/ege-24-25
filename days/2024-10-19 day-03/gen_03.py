from random import randint as rnd


cnt = 1_000
nums = [rnd(1, 100) for _ in range(cnt)]

f = open('./nums.txt', 'w')
lines = [f"{num}\n" for num in nums]
f.writelines(lines)

"""
найти кол-во чисел кратных 3
"""
