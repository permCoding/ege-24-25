def f(x):
    return (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))

P = list(range(15, 41))
Q = list(range(21, 63))

A = []
for x in range(10, 70):
    if f(x) == False:
        A.append(x)
print(len(A), A)  # 20 точек
print(A[-1]-A[0])  # 19 длина отрезка