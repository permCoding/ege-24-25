def f():
    for a in range(1, 80):
        for b in range(1, 80):
            for c in range(1, 80):
                s = '>' + a*'1' + b*'2' + c*'3'

                while ('>1' in s) or ('>2' in s) or ('>3' in s):
                    if ('>1' in s): s = s.replace('>1','21>3', 1)
                    if ('>2' in s): s = s.replace('>2','32>', 1)
                    if ('>3' in s): s = s.replace('>3','11>2', 1)
                if s.count('1') == 71 and s.count('2') == 54 and s.count('3') == 37:
                    return a,b,c
        print(a)

print(f())
