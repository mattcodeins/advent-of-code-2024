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
prev = {(0,start):{start}}
while q:
    d, p, dir = q.pop(0)
    if G[p] == 'E':
        print(d)
        print(len(prev[(d,p)]))
        break
    if (p,dir) in seen:
        continue
    seen.add((p,dir))
    for x, ndir in p.steps(included=True):
        if G[x] == '#':
            continue
        nd = d+1 if dir == ndir else d+1001
        prev[(nd,x)] = prev.get((nd,x),{x}) | prev[(d,p)]
        q.append((nd, x, ndir))
    q.sort(key=lambda x: x[0])