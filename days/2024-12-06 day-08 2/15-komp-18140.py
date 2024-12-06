def f(A, x, y):
    return (x-y>=39) or (y <= x) or (y >= A-20)

for A in range(900, -1, -1):
    if all(f(A, x, y) for x in range(1, 900) for y in range(1, 900)):
        print(A)  # 22
        break

# for A in range(200, -1, -1):
#     b = True
#     for x in range(1, 200):
#         for y in range(1, 200):
#             if f(A, x, y) == False:
#                 b = False
#                 break
#     if b:
#         print(A)  # 22
#         break
