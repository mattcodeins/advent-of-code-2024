from utils import *

inp, size = readlines('day14/input.txt'), V(101, 103)
# inp, size = readlines('day14/test.txt', prnt=True), V(11,7)

def printgrid(size, guards):
    grid = [['.' for _ in range(size.x)] for _ in range(size.y)]
    for g in guards:
        if grid[g.y][g.x] == '.':
            grid[g.y][g.x] = '1'
        else:
            grid[g.y][g.x] = str(int(grid[g.y][g.x]) + 1)
    for row in grid:
        print(''.join(row))
    print()

ps, vs = [], []
for p,v in inp:
    p = V(*p[2:].split(','))
    v = V(*v[2:].split(','))
    ps.append(p)
    vs.append(v)

for n in range(1, 10000):
    c = defaultdict(int)
    prnt = True
    for i, p in enumerate(ps):
        v = vs[i]
        p.x = (p.x + v.x) % size.x
        p.y = (p.y + v.y) % size.y
        c[p] += 1
        if c[p] > 1:
            prnt = False
    if prnt:
        printgrid(size, ps)
        print(n)
        break
