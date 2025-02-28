def get_divs(n):
    divs = set()
    for d in range(2, int(n**.5)+1):
        if n%d == 0:
            divs.add(d)
            divs.add(n//d)
    return sorted(divs)

k = 0
for n in range(800_000, 10**10):
    divs = get_divs(n)
    M = 0
    if len(divs) > 0:
        M = divs[0] + divs[-1]
    if M%10 == 4:
        print(n, M)
        k += 1
    if k > 4:
        break