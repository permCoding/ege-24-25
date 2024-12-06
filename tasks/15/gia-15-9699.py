def solve_1():
    A = []
    for x in range(1, 30):
        if (((x in P) and (x in Q)) <= (x in A)) == False:
            A.append(x)
    print(A[-1]-A[0], A)
    

def solve_2():
    def f(A, x):
        return ((x in P) and (x in Q)) <= (x in A)
    res = []
    for l in range(1, 30):
        for r in range(l+1, 30):
            A = list(range(l, r+1))
            if all(f(A, x) for x in range(1, 30)):
                res.append(len(A)-1)  # это точки, а -1 это расстояние между точками
    print(min(res))
    
P = list(range(4, 16))
Q = list(range(12, 21))

# solve_1()
solve_2()
