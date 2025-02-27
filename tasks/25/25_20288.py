for n in range(9231*2, 10**10+1, 9231):
    s = str(n)
    if s[-2]=='4' and s[-5:-3]=='12':
        if int(s[-1])%2==1 and int(s[-3])%2==1:
            if all(int(e)%2==0 for e in s[0:-5]):
                print(n, n//9231)
        