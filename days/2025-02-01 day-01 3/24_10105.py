def solver_1():
    s = 'T' + open('./24_10105.txt').readline() + 'T'
    t = [i for i in range(len(s)) if s[i] == 'T']
    print(max(t[i+101]-t[i]-1 for i in range(len(t)-101)))  # 133

def solver_2():
    s = open('./24_10105.txt').readline() + '-'
    l, r = 0, 1
    mx = 2
    cnt = 2
    while r < len(s)-5:
        if l%1_000_000 == 0: print(l, r, mx)
        while cnt <= 100:
            if r < len(s)-1:
                r += 1
                if s[r] == 'T': cnt += 1
                if cnt == 100: mx = max(mx, r-l+1)
        while cnt > 100:
            if s[l] == 'T':
                cnt -= 1
            l += 1
    print(mx)

solver_1()
##solver_2()

'''
Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
Определите максимальное количество идущих подряд символов,
среди которых символ T встречается ровно 100 раз.

    1)  2 - T
        012345678901234
        UUTUTTUUUUTUUUU
    lst   0 12    3
        ln1 = lst[3]-lst[0]-1
        ln2 = lst[4]-lst[1]-1
        ln3 = lst[5]-lst[2]-1
        
    2) левая и правая метки
        UUTUTTUUUUTUUUUT
'''
