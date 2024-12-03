def f(A, x):
    return (((x%12==0) or (x%36==0)) <= (x%A==0)) and (A**2-A-90<0)


t = []
for A in range(1, 200):
    b = True
    for x in range(0, 200):
        if f(A, x) == False:
            b = False
            break
    if b: t.append(A)
print(max(t))  # 6

t = []
for A in range(1, 200):
    if all(f(A, x) for x in range(0, 200)):
        t.append(A)
print(max(t))  # 6
    
"""

"""