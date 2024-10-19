nums = [int(e) for e in open('./demo_2025_17.txt')]

mn = 2**30
for num in nums:
    if num < mn:
        mn = num

print(mn)
