nums = [int(e) for e in open('./demo_2025_17.txt')]

mn = min(nums)

k, max_p = 0, 0
for i in range(0, len(nums)-1):
    if nums[i]%16 == mn or nums[i+1]%16 == mn:
        k += 1
        if nums[i]+nums[i+1] > max_p:
            max_p = nums[i]+nums[i+1]

print(k, max_p)







# len(nums)-2  len(nums)-1
# 1 2 3 4 5
# 0 1 2 3 4

"""
a b OR
0 0  0
0 1  1
1 0  1
1 1  1
"""
