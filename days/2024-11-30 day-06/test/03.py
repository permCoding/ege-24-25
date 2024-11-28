ref = [list(map(int, line.split('\t'))) for line in open('./03_связи.txt')]

ppl = [[int(line.split('\t')[0]), line.split('\t')[1]] for line in open('./03_люди.txt')]
dct = dict(ppl)

children = [e[1] for e in ref if dct[e[0]] == dct[e[1]]]

print(len(set(children)))
