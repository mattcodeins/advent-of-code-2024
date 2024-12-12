from utils import *

inp = readlines('day12/input.txt')
inp = readlines('day12/test.txt')
grid = M(inp)
# print(grid)
seen = set()

def fill(i,c):
    global seen
    if i in seen:
        return 0, 0
    seen.add(i)
    area, perimeter = 0, 0
    area += 1
    for ni in i.steps():
        if grid[ni] == c:
            a, p = fill(ni,c)
            area += a
            perimeter += p
        else:
            perimeter += 1
    return area, perimeter

cost = 0
for i, v in grid:
    if i in seen:
        continue
    a, p = fill(i,v)
    cost += a*p
print(cost)