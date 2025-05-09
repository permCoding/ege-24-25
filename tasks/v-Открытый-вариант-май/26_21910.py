f = open('./26_21910.txt')
n = int(f.readline())
nums = sorted(int(s) for s in f)
nums = nums[::-1]

t = [nums[0]]
for e in nums[1:]:
    if t[-1] - e >= 9:
        t += [e]
print(len(t), t[-1])  # 1040 57