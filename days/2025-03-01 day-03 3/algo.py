"""
найти ближайшее большее целое чем n
кратное 13 и чётное
"""

n = 23
i = 24
while not(i%13 == 0 and i%2 == 0):
    i += 1
print(i)

# for i in range(24, 1_000):
#     if i%13 == 0 and i%2 == 0:
#         print(i)
#         break

# for i in range(13, 1_000, 13):
#     if i > n:
#         if i%2 == 0:
#             print(i)
#             break

lst = []
for i in range(24, 1_000):
    if i%13 == 0 and i%2 == 0:
        lst.append(i)
print(min(lst))

print(min(i for i in range(24, 1_000) if i%13 == 0 and i%2 == 0))
