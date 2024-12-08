from utils import *

lines = readlines('day08/input.txt', sep=' ', prnt=False)
# lines = readlines('day08/test.txt', sep=' ')
g = defaultdict(str) | {(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))}

digittolocs = defaultdict(set)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if g[i,j] != ".":
            digittolocs[g[i,j]].add((i,j))


def solve(p1=True):
    antinodes = set()
    for d, locs in digittolocs.items():
        for l1 in locs:
            for l2 in locs:
                if l1 == l2:
                    continue
                d1 = l1[0]-l2[0]
                d2 = l1[1]-l2[1]
                if p1:
                    x = l2[0] + 2*d1
                    y = l2[1] + 2*d2
                    if g[x,y]:
                        antinodes.add((x,y))
                else:
                    i = 1
                    while True:
                        x = l2[0] + i*d1
                        y = l2[1] + i*d2
                        if g[x,y]:
                            antinodes.add((x,y))
                        else:
                            break
                        i += 1
    return len(antinodes)

print(solve())
print(solve(False))