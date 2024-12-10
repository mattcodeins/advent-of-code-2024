from utils import *

lines = readlines('day10/input.txt', sep=-1)
# lines = readlines('day10/test.txt', sep=-1)

g = defaultdict(int) | {(i,j):x for i, l in enumerate(lines) for j, x in enumerate(l)}

heads = []
for i, x in g.items():
    if x == 0:
        heads.append(i)

def solve(p1=True):
    r = 0
    for h in heads:
        found = set()
        q = deque([h])
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                    ni = (i[0]+d[0], i[1]+d[1])
                    if g[ni] and g[ni] == g[i]+1:
                        if g[ni] == 9:
                            if p1:
                                found.add(ni)
                            else:
                                r+=1
                        q.append(ni)
        if p1:
            r += len(found)
    return r

print(solve())
print(solve(False))