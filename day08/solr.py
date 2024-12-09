from utils import *

# lines = readlines('day08/input.txt', sep=' ')
# lines = readlines('day08/test.txt', sep=' ')
g = M('day08/input.txt')

digittolocs = defaultdict(set)
for i, p in g:
    if p != ".":
        digittolocs[p].add(i)


def solve(p1=True):
    antinodes = set()
    for _, locs in digittolocs.items():
        for l1 in locs:
            for l2 in locs:
                if l1 == l2:
                    continue
                v = l2 - l1
                if p1:
                    x = l1 + 2*v
                    if g[x]:
                        antinodes.add(x)
                else:
                    i = 1
                    while True:
                        x = l1 + i*v
                        if g[x]:
                            antinodes.add(x)
                        else:
                            break
                        i += 1
    return len(antinodes)

print(solve())
print(solve(False))