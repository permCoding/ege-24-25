cnt = 10
f = open('./nums.txt', 'w')

nums = [12,34,56,78,90]
for num in nums:
    # f.write(str(num)+'\n')
    f.write(f"{num}\n")
