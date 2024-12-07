from utils import *

lines = readlines('day06/input.txt', sep='', prnt=False)
lines = readlines('day06/test.txt', sep='')

grid = Grid([list(l) for l in lines], '^', '3')

obs = {i+j*1j for i,r in enumerate(lines) for j,x in enumerate(r) if x == '#'}
graph = {}
dirs = [1,-1j,-1,1j]
for o in obs:
    for i, d in enumerate(dirs):
        x = o+d
        # while grid[x] and

start_time = time.time()
def solve(ob=None):
    p, d = s, -1
    seen = set()
    seendir = set()
    while grid[p]:
        if (p,d) in seendir:
            return 0
        seen.add(p)
        seendir.add((p,d))
        while grid[p+d] == '#' or p+d == ob:
            d *= -1j
        p += d
    return seen

seen = solve()
print(len(seen))

part2 = set()
for ob in seen:
    if grid[ob] == '.' and not solve(ob):
        part2.add(ob)
print(len(part2))
print("--- %s seconds ---" % (time.time() - start_time))