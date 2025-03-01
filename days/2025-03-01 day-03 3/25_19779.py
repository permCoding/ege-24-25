def get_divs(n):
    st = set()
    for div in range(2, int(n**.5)+1):
        if n%div == 0:
            st.add(div)
            st.add(n//div)
    return st


k = 0
n = 55_000_000
while k < 4:
    n += 1
    
    for div in get_divs(n):
        if div%1_000 == 777 and len(get_divs(div)) == 0:
            print(n, div)
            k += 1


# n = 321_987
# print(n%10)
# print(n%100)
# print(n%1000)
