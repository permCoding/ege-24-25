# 1 - 01234 циклом по 5-чной СС

# print(int('44444', 5))  # 3124

def get(dec):
    res = ''
    while dec > 0:
        res = str(dec % 5) + res
        dec //= 5
    return res

for dec in range(0, 3125):
    s = get(dec)
    if len(s) == 5 and s.count('4') == 0 and s.count('3') == 2:
        print(dec+1, s)

# print(get(6))


# ФКККК

# 33222
# 33333

# 34444
# 40000