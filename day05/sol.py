from utils import *

lines = readlines('day05/input.txt')
# lines = readlines('day05/test.txt')

orders = lines[0]
ord = defaultdict(set)
for o in orders:
    b,a = o.split("|")
    ord[int(b)].add(int(a))

middles = []
incorrects = []
for u in lines[1]:
    bad = False
    x = u.split(",")
    x = [int(aa) for aa in x]
    seen = set()
    for y in x:
        after = ord[y]
        for s in seen:
            if s in after:
                bad=True
        seen.add(y)
    if not bad:
        middles.append(x[len(x)//2])
    else:
        incorrects.append(x)

print(sum(middles))

res = []
for x in incorrects:
    for i, y in enumerate(x):
        after = ord[y]
        for j in range(i):
            if x[j] in after:
                x[i], x[j] = x[j], x[i]
    res.append(x)

middles = [x[len(x)//2] for x in res]

print(sum(middles))