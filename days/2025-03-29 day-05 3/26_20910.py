f = open('./26_20910_.txt')
n, m, k = map(int, f.readline().split())

cols = [m] + [m] * k
for line in f:
    row, col = map(int, line.split())
    if row < cols[col]:
        cols[col] = row

pairs = []
for col in range(k):
    pairs.append(min(cols[col], cols[col+1]) - 1)
    
print(pairs)

print(max(pairs))

"""
доделать вывод:
наименьший номер места в найденной паре кресел
"""