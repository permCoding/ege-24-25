for n in range(4, 10_000):
    s = '1' + n * '2'
    while '12' in s or '322' in s or '222' in s:
        if '12' in s: s = s.replace('12', '2', 1)
        if '322' in s: s = s.replace('322', '21', 1)
        if '222' in s: s = s.replace('222', '3', 1)

    # sm = 0
    # for i in range(len(s)):
    #     sm += int(s[i])

    # sm = 0
    # for e in s:
    #     sm += int(e)

    sm = sum(int(e) for e in s)

    if sm == 15:
        print(n)
        break
    
