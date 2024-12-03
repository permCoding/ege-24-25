# ответа нет
def f(x):
    inP = 13 <= x <= 19
    inQ = 17 <= x <= 23
    a = not(not(inP) <= inQ)
    b = True <= (not(inQ) <= inP)
    return a <= b

for x in range(13, 23+1):
    print(x, f(x))


# def f(x, l, r):
#     inP = 13 <= x <= 19
#     inQ = 17 <= x <= 23
#     inA = l <= x <= r
#     a = not(not(inP) <= inQ)
#     b = inA <= (not(inQ) <= inP)
#     return a <= b

# t = [(13,17), (13,19), (13,23), (17,19), (17, 23), (19, 23)]
# l, r = t[2]
# for x in range(l, r+1):
#     print(x, f(x, l, r))


# def f(x, inA):
#     x += .5
#     inP = 13 <= x <= 19
#     inQ = 17 <= x <= 23
#     a = not(not(inP) <= inQ)
#     b = inA <= (not(inQ) <= inP)
#     return a <= b

# for x in range(10, 25):
#     print(x, f(x, False), f(x, True))

    
# def f(x, l, r):
#     inP = 13 <= x <= 19
#     inQ = 17 <= x <= 23
#     inA =  l <= x <=  r
#     a = not(not(inP) <= inQ)
#     b = inA <= (not(inQ) <= inP)
#     return a <= b

# t = []
# for l in range(100, 250):
#     for r in range(100, 250):
#         if all(f(x/10, l/10, r/10) for x in range(100, 250)):
#             t.append(r/10-l/10)
# print(max(t))
    
"""
https://education.yandex.ru/ege/task/21fef5ec-ac54-4333-b360-20a22600f6c8
"""