def f(a, b, way=''):
    if a < b: return 0
    if '111' in way or '222' in way: return 0
    if a == b: return 1
    if a%2 == 0:
        return f(a-2, b, way+'1') + f(a//2, b, way+'2')
    else:
        return f(a-2, b, way+'1') + f(a-7, b, way+'2')

print(f(40, 1))
