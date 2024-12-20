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

def is_tree(ps):
    c = 0
    s = set(ps)
    for i in range(size.x):
        for j in range(size.y):
            if V(i,j) in s:
                c += 1
                if c == 10:
                    return True
            else:
                c = 0
    return False

ps, vs = [], []
for p,v in inp:
    p = V(*p[2:].split(','))
    v = V(*v[2:].split(','))
    ps.append(p)
    vs.append(v)

for n in range(1, 10000):
    for i, p in enumerate(ps):
        v = vs[i]
        p.x = (p.x + v.x) % size.x
        p.y = (p.y + v.y) % size.y
    if is_tree(ps):
        printgrid(size, ps)
        print(n)
        break
