M = list(range(32, 69))
N = list(range(54, 76))

A = []
for x in range(30, 80):
    f = not((x in M) or (x in N)) == (not(x in A))
    if f == False:
        A.append(x)
print(len(A), A)  # 44
