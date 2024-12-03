def get_d(n):
    t = []
    for d in range(2, int(n**.5)+1):
        if n%d==0: t += [d, n//d]
    return list(set(t))
    
def p(n):
    for d in range(2, int(n**.5)+1):
        if n%d==0: return False
    return True

for n in range(326782, 965325):
    t = get_d(n)
    w = [d for d in t if p(d)]
    if len(w) == 3:
        if w[0]*w[1]*w[2]==n:
            diff = max(w)-min(w)
            if diff <= 12: print(n, diff)
"""
347261 6
375803 12
386389 12
409457 8
430189 12
465547 12
478661 10
583573 10
871933 12
"""