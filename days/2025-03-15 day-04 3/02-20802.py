for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (w <= (not(z <= x))) or y
                if f == False:
                    print(z,x,y,w, ' ', int(f))







# x = False
# y = not(x)
# print(x, y)

# lst = [ 
#     (0, 0),
#     (0, 1),
#     (1, 0),
#     (1, 1)
# ]
# for x, y in lst:
#     # print(x, y, x or y)
#     # print(x, y, x and y)
#     # print(x, y, x ^ y)  # XOR - либо
#     print(x, y, int(x <= y))

# for x in 0,1:
#     for y in 0,1:
#         print(x, y, x or y)
        # print(x, y, x and y)
        # print(x, y, x ^ y)  # XOR - либо
        # print(x, y, int(x <= y))
