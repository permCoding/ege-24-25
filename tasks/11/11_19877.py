"""txt
4 
op = id + os + di
id = 20 bit => 4 ANGL (26)
os = 70 * 11 bit
di = x byte

131072 object => 24 Mbyte
1 object => Y byte

Y = 192 byte
id+os=20+770=790 bit
192 byte - 790 / 8
"""

print(24*1024*1024/131072)
print(192-790/8)