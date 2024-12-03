nums = [int(e) for e in open('nums.txt')]
avg = sum(nums) / len(nums)

print(len( [num for num in nums if num > avg] ))

"""
найти кол-во чисел
больших чем среднее
арифметическое в файле
"""
