from utils import *

lines = readlines('day06/input.txt', sep=-1)
# lines = readlines('day06/test.txt', sep='')

for i, r in enumerate(lines):
    for j, x in enumerate(r):
        if x == "^":
            s = i+j*1j
grid = defaultdict(str) | {(i+j*1j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))}

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