for n in range(9231, 10**10+1, 9231):
    s = str(n)
    if len(s) >= 5 and s[-2] == '4' and s[-5:-3] == '12':
        if s[-3] in '13579' and s[-1] in '13579':

            # check = True
            # for e in s[:-5]:
            #     if int(e)%2 != 0:
            #         check = False
            
            # if check:
            #     print(n, n//9231)

            # if all(e in '02468' for e in s[:-5]):
            #     print(n, n//9231)
            
            if all(map(lambda e: e in '02468', s[:-5])):
                print(n, n//9231)

        
# *12?4?
# 12141