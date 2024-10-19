k = 0
for line in open('nums.txt'):
    if int(line)%3 == 0:
        k += 1
print(k)


"""
найти кол-во чисел
больших чем среднее
арифметическое в файле
"""