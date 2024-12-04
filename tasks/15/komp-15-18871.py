P = list(range(15, 40))
Q = list(range(21, 63))

A = []
for x in range(10, 70):
    f = (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))
    if f == False:
        A.append(x)
print(len(A), A)  # 44
