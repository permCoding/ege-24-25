def get_div(n):
    st = set()
    for d in range(2, int(n**0.5)+1):
        if n%d == 0:
            st.add(d)
            st.add(n//d)
    return st

n = 55_000_000  # 1.5 sec
k = 0
while k < 4:
    n += 1
    for d in get_div(n):
        if d%1000==777 and len(get_div(d))==0:
            print(n, d)
            k += 1
            break


# n = 55_000_000  # 45 sec
# k = 0
# while k < 4:
#     n += 1
#     # print(n)
#     d = 0
#     while True:
#         d777 = int(str(d) + '777')
#         if n%d777==0:
#             check = True
#             for r in range(2, d777//2+1):
#                 if d777%r==0:
#                     check = False
#                     break
#             if check:
#                 print(n, d777)
#                 k += 1
#         d += 1
#         if d777 > n//2+1:
#             break
