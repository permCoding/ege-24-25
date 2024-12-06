def solve_1():
    def f(A, x):
        return (x&57==0) or ((x&23==0) <= (not(x&A==0)))

    for A in range(1, 900):
        b = True
        for x in range(1, 900):
            if f(A, x) == False:
                b = False
                break
        if b:
            print(A)  # 40
            break

def solve_2():
    def f(A, x):
        return (x&57==0) or ((x&23==0) <= (not(x&A==0)))

    for A in range(1, 900):
        if all(f(A, x) for x in range(1, 900)):
            print(A)  # 40
            break
    
    
solve_2()

"""
14 => 1110
 5 => 0101
      ----
      0100 => 4

x y &
0 0 0
0 1 0
1 0 0
1 1 1

x y →
0 0 1
0 1 1
1 0 0
1 1 1

x f
0 1
1 0
"""