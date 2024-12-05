s = '00011001'
r = int(s, 2)
print(r)

n = 20
# r = bin(n)[2:]
r = f'{n:b}'
print(r)

print(int('13', 8))
print(int('206', 8))
print(int('10', 16))
print(f'{10:x}')
print(int('2A', 16))

al2 = '01'  # 2
al8 = '01234567'  # 8
al10 = '0123456789'  # 10
al16 = '0123456789ABCDEF'  # 16

d = int('106', 8)
print(hex(d))

"""
106(8) => 001 000 110 (2) =>  46 (16)




1 0
8 1
1 3 (8) => 1*8 + 3*1 = 11 (10)


00
01
02
03
04
05
06
07 +1
10 +1
11 +1
12 +1
13 +1


206 (8)
2*64 + 6*1 = 128 + 6 = 134 (10)


10 (16) != 10 (10)
10 (16) == 16 (10)

   0
   1
   2
   3
   4
   5
   6
   7
   8 +1
09 9 +1
10 A +1
11 B
12 C
13 D +1
14 E +1
15 F +1
16 => 10


2A (16) => __ (10)
2*16**1 + A*16**0 => 32 + 10 = 42



87654321
76543210
00011001


1*2**4 + 1*2**3 + 0*2**2 + 0*2**1 + 1*2**0
  16   +   8    +    0   +    0   +   1
"""