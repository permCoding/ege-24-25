def f(s, step):
    if s >= 132: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [
            f(s+3, step),
            f(s+6, step),
            f(s*3, step)
        ]
    if step%2 != 0:
        #return any(t)  # 19
        return all(t)
    else:
        return any(t)


for s in range(1, 132):
    # if f(s,2):  # 19 => 41
    # if not(f(s,1)) and f(s,3):  # 20 => 14 35
    if not(f(s,2)) and f(s,4):  # 21 => 32
        print(s)
        #break
