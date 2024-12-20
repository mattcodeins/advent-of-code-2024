from utils import *
import time

start_time = time.time()
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
        seen.add(p)
        for x, s in p.steps(included=True):
            if G[x] != "#":
                q.append(x)
        skipq = deque([p])
        for i in range(21):
            for _ in range(len(skipq)):
                sp = skipq.popleft()
                if (p, sp) in savedt:
                    continue
                st = -1
                if sp in dtoend:
                    st = noskipd - (dtoend[sp]+d+i)
                savedt[(p, sp)] = st
                for x in sp.steps():
                    skipq.append(x)
    d += 1

res = 0
for d in savedt.values():
    if d >= 100:
        res += 1
print(res)

print("--- %s seconds ---" % (time.time() - start_time))