nums = [int(s) for s in open('./17_21416.txt')]

sm = sum(num for num in nums if num < 0)

lst = []
for i in range(len(nums)-2):
    if max(nums[i:i+3])*min(nums[i:i+3]) > sm:
        lst.append(sum(nums[i:i+3]))

print(len(lst), abs(max(lst)))