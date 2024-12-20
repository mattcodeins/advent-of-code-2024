from utils import *

inp = readlines('day20/input.txt')
# inp = readlines('day20/test.txt', prnt=True)

G = M(inp)

for i, x in G:
    if x == "E":
        end = i
    if x == "S":
        start = i

dtoend = {}
q = deque([end])
d = 0
while q:
    for _ in range(len(q)):
        p = q.popleft()
        if p in dtoend:
            continue
        dtoend[p] = d
        for x in p.steps():
            if G[x] != "#":
                q.append(x)
    d += 1

noskipd = dtoend[start]
d = 0
q = deque([start])
savedt = {}
seen = set()
while q:
    for _ in range(len(q)):
        p = q.popleft()
        if p in seen:
            continue
        for x, s in p.steps(included=True):
            if x+s in dtoend:
                st = noskipd - (dtoend[x+s]+d+2)
                if st > 0:
                    savedt[(p, x+s)] = st
            if G[x] != "#":
                q.append(x)
        seen.add(p)
    d += 1

res = 0
for d in savedt.values():
    if d >= 100:
        res += 1
print(res)