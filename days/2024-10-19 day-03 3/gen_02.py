cnt = 10
f = open('./nums.txt', 'w')

nums = [12,34,56,78,90]
lines = [f"{num}\n" for num in nums]

f.writelines(lines)
