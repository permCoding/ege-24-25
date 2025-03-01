k = 0
n = 902714
while k < 6:
    n += 1
    
    for div in range(15, n, 10):
        if n%div == 0:
            print(n, div)
            k += 1
            break

        
"""
n = 9
1 3 9
1 2 4 8 16

"""