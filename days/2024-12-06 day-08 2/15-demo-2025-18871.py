def f(x):
    return (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))


P = list(range(15, 41))
Q = list(range(21, 64))
A = []
for x in range(10, 70):
    if f(x) == False:
        A += [x]
        # A.append(x)
print(len(A)-1)  # 19

"""
x = 36

# P = 15 <= x <= 40
# print(P)

# P = [x for x in range(15, 41)]
# print(x in P)

P = list(range(15, 41))
print(x in P)
"""