# S = 1280 * 960  # уже сжатое px => RGB
# K = 8  # bit/px
# B = S * K  # print(S*8)
# T = B / V  # <= 30 sec

T = 30
V = 164_000  # бит/сек
S = 4 * T * V
R = 1280 * 960
print(S / R)
print(2 ** 16)

# = 30 * 164_000 / 1280 * 960