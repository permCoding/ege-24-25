nums = [int(s) for s in open('./17_21416.txt')]

sum_ = sum(e for e in nums if e < 0)

cnt, mx_sm = 0, -2**32
for i in range(len(nums)-2):
    t = nums[i:i+3]
    if max(t)*min(t) > sum_:
        cnt += 1
        mx_sm = max(mx_sm, sum(t))

print(cnt, abs(mx_sm))  # 10007 7953
