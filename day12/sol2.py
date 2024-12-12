from utils import *

inp = readlines('day12/input.txt')
# inp = readlines('day12/test.txt')
grid = M(inp)
# print(grid)
seen = set()

def fill(i,c):
    global seen
    if i in seen:
        return set()
    seen.add(i)
    r = {i}
    for ni in i.steps():
        if grid[ni] == c:
            r |= fill(ni,c)
    return r

regions = []
for i, v in grid:
    if i in seen:
        continue
    regions.append(fill(i,v))

cost = 0
for reg in regions:
    sides = 0
    start = V(min([i[0] for i in reg]), min([i[1] for i in reg]))
    end = V(max([i[0] for i in reg]), max([i[1] for i in reg]))
    for i in range(start[0], end[0]+1):
        ns = 0
        bl, br = True, True
        for j in range(start[1], end[1]+1):
            if V(i,j) in reg:
                l = V(i-1,j) in reg
                if not l and bl:
                    sides += 1
                bl = l
                r = V(i+1,j) in reg
                if not r and br:
                    sides += 1
                br = r
            else:
                bl, br = True, True
        sides += ns

    for j in range(start[1], end[1]+1):
        ns = 0
        bl, br = True, True
        for i in range(start[0], end[0]+1):
            if V(i,j) in reg:
                l = V(i,j-1) in reg
                if not l and bl:
                    sides += 1
                bl = l
                r = V(i,j+1) in reg
                if not r and br:
                    sides += 1
                br = r
            else:
                bl, br = True, True
        sides += ns
    cost += sides*len(reg)
print(cost)