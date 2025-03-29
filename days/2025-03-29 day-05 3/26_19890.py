# f = open('./26_19890_.txt')
f = open('./26_19890.txt')
k, g = map(int, f.readline().split())

v1, v2 = [], []
for line in f:
    num = int(line)
    if 310 <= num <= 320:
        v1 += [num]
    else:
        v2 += [num]
v = v1 + sorted(v2)
# print(v)
m = 0
cnt = 0
for i in range(len(v)):
    if m + v[i] <= g:
        m += v[i]
        cnt += 1
print(cnt)  # 129
# print(m)
m -= v[cnt-1]
for pos in range(len(v)-1, cnt-2, -1):
    if m + v[pos] <= g:
        print(m + v[pos])  # 10_000
        break

# lst = [8,1,2,3,7,9,4,5,6,]
# lst.sort()
# print(lst)
# g = 10
# m = 0
# cnt = 0
# for i in range(len(lst)):
#     if m + lst[i] <= g:
#         m += lst[i]
#         cnt += 1
# print(m, cnt)

