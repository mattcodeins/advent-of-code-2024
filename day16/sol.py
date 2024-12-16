from utils import *

inp = readlines('day16/input.txt')
# inp = readlines('day16/test.txt')

G = M(inp)
for i, x in G:
    if x == 'S':
        start = i
        break

q = [(0, start, V(0,1))]
seen = set()
while q:
    d, p, dir = q.pop(0)
    if G[p] == 'E':
        print(d)
        break
    if (p,dir) in seen:
        continue
    seen.add((p,dir))
    for x, ndir in p.steps(included=True):
        if G[x] == '#':
            continue
        if dir == ndir:
            q.append((d+1, x, ndir))
        else:
            q.append((d+1001, x, ndir))
    q.sort(key=lambda x: x[0])