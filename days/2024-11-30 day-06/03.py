rel = [line[:-1].split('\t') for line in open('./03-1.txt')]
ppl = [line.split('\t') for line in open('./03-2.txt')]

dct = dict(ppl)

# children = [elm[1] for elm in rel if dct[elm[0]] == dct[elm[1]]]
# print(len(set(children)))

flt = filter(lambda pair: dct[pair[0]] == dct[pair[1]], rel) 
print(len(set(map(lambda pair: pair[1] , flt))))


""" 38
количество людей, 
которые родились в том же городе, 
что и хотя бы один из их родителей
"""