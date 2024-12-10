from utils import *

lines = readlines('day10/input.txt', sep=-1)
# lines = readlines('day10/test.txt', sep=-1)

g = M(lines)
heads = [h for h, x in g if x == 0]

def solve(p1=True):
    r = 0
    for h in heads:
        res = g.bfs(h, lambda np,p: g[np]==g[p]+1, lambda np,_: g[np]==9)
        r += len(set(res)) if p1 else len(res)
    return r

print(solve())
print(solve(False))