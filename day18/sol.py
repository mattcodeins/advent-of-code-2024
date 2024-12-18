from utils import *

test = None
# test = 'day18/test.txt'
fp = 'day18/input.txt' if not test else test
inp = readlines(fp, sep=',')
size = 6 if test else 70

idx = 12 if test else 1024
blocks =[V(*x) for x in inp]
goal = V(size,size)

def bfs(blocks, goal):
    q = deque([V(0,0)])
    d = 0
    seen = set()
    while q:
        for _ in range(len(q)):
            p = q.popleft()
            if p in seen:
                continue
            seen.add(p)
            if p == goal:
                return d
            if p.x < 0 or p.y < 0 or p.x > size or p.y > size:
                continue
            if p in blocks:
                continue
            q.extend(p.steps())
        d += 1
    return False

print(bfs(blocks[:idx], goal))

def binary_search(idx, blocks, goal):
    l, r = idx, len(blocks)
    while l < r:
        m = (l+r)//2
        if bfs(blocks[:m], goal):
            l = m+1
        else:
            r = m
    return l-1

x = binary_search(idx, blocks, goal)
print(blocks[x])