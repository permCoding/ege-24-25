def f0():
    a = [61, 58, 73, 42]
    b = [61, 58, 75, 136]
    print(f'{a[2]:b}'.rjust(8, '0'))
    print(f'{b[2]:b}'.rjust(8, '0'))

    b1, b2, b3, b4 = 61, 58, 72, 0  # адрес сети
    print(f'{b1}.{b2}.{b3}.{b4}')    
    net = f'{b1:b}.{b2:b}.{b3:b}.{b4:b}'
    print(net.count('1'))  # их нечётное кол-во
    t = [1 for n in range(1, 1023) if f'{n:b}'.count('1')%2 == 0]
    print(len(t))  # 0 и 1023 нельзя


def f1(a, b):
    a = list(map(int, a.split('.')))
    b = list(map(int, b.split('.')))
    m = (255, 255, int('11111100', 2), 0)

    print(f'{a[2]:b}'.rjust(8, '0'))
    print(f'{b[2]:b}'.rjust(8, '0'))
    print(f'{b[1]:b}'.rjust(8, '0'))

    print(m[0]&a[0], m[1]&a[1], m[2]&a[2], m[3]&a[3])
    print(m[0]&b[0], m[1]&b[1], m[2]&b[2], m[3]&b[3])

    # 00 00000000 - это адрес сети
    # 00 00000001
    # ... 
    # 11 11111110
    # 11 11111111 - это широковещательный
    # 2**10 / 2 = 512 - 2 = 510 ...
    b1, b2, b3 = 61, 58, 72
    net = f'{b1:b}{b2:b}{b3:b}'
    print(net.count('1'))  # их нечётное кол-во
    k = 0
    for ost in range(1, 1023):
        if f'{ost:b}'.count('1')%2 == 0:
            k += 1
    print(k)

def f2(a, b):
    from ipaddress import ip_network

    for mask in range(16, 33):  # кол-во 1 слева
        net_a = ip_network(a + '/' + str(mask), False)
        net_b = ip_network(b + '/' + str(mask), False)
        if net_a == net_b:
            print(mask, net_b)

a = '61.58.73.42'
b = '61.58.75.136'
f0()
# f1(a, b)
# f2(a, b)


"""
61.58.73.0 - это адрес самой сети
61.58.73.255 - это адрес широковещательный,
для рассылки данных всем узлам в этой сети
"""