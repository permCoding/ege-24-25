x = 6*25**1013 + 3*125**1004 - 4*5**2001 + 2024

lst = []
while x > 0:
    ost = x % 25
    x //= 25
    
    lst.append(ost)

sm = 0
for elm in lst:
    sm += elm
    if elm != 0:
        print(elm)
print(sm)
