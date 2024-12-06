al = '0123456789' + ''.join(chr(e) for e in range(65, 84))

for x in al:
    a = f'42{x}158'
    b = f'16{x}234'
    r = int(a, 29) + int(b, 29)
    if r%28 == 0:
        print(r//28)  # 3882305

"""
https://education.yandex.ru/ege/task/de1be318-922d-4bc9-a58a-aeabbecdf01b
"""
