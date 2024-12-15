from calendar import c
from utils import *

inp = readlines('day15/input.txt')
# inp = readlines('day15/test.txt')

def convert_grid(inp):
    r = []
    for row in inp:
        ri = []
        for x in row:
            if x == '#':
                ri.append('##')
            elif x == '.':
                ri.append('..')
            elif x == 'O':
                ri.append('[]')
            elif x == '@':
                ri.append('@.')
        r.append([y for y in ''.join(ri)])
    return M(r)

def score(G):
    r = 0
    for i, x in G:
        if x == '[':
            r += i.x*100 + i.y
    return r

def boxside(x):
    if x == '[':
        return ']'
    if x == ']':
        return '['

def move(i, d, G):
    j = i+d
    x = 0
    s = ''
    while G[j] == ']' or G[j] == '[':
        if not s:
            s = G[j]
        x += 1
        j = j+d
    if G[j] == '#':
        return G, i
    if G[j] == '.':
        for _ in range(x):
            s = boxside(s)
            G[j] = s
            j -= d
        G[j] = '@'
        G[i] = '.'
        return G, j
    
def bfs(q, ls, rs, d, G):
    while q:
        l = []
        r = []
        for _ in range(len(q)):
            i = q.popleft()
            j = i+d
            if G[j] == '[':
                l.append(j)
                r.append(j+V(0,1))
                q.append(j)
                q.append(j+V(0,1))
            if G[j] == ']':
                r.append(j)
                l.append(j+V(0,-1))
                q.append(j)
                q.append(j+V(0,-1))
            if G[j] == '#':
                return G, False
        ls.append(l)
        rs.append(r)
    ls = reversed(ls)
    rs = reversed(rs)
    for l,r in zip(ls,rs):
        for i in l:
            G[i+d] = '['
            G[i] = '.'
        for i in r:
            G[i+d] = ']'
            G[i] = '.'
    return G, True

def move2(i, d, G):
    j = i+d
    ismove = True
    if G[j] == '[':
        ls, rs = [[j]], [[j+V(0,1)]]
        q = deque([j, j+V(0,1)])
        G, ismove = bfs(q, ls, rs, d, G)
    elif G[j] == ']':
        ls, rs = [[j+V(0,-1)]], [[j]]
        q = deque([j+V(0,-1), j])
        G, ismove = bfs(q, ls, rs, d, G)
    if G[j] == '#' or not ismove:
        return G, i
    else:
        G[j] = '@'
        G[i] = '.'
        return G, j

G = convert_grid(inp[0])

for i, x in G:
    if x == '@':
        robot = i
        break
moves = ''.join(inp[1])

for m in moves:
    if m == '<':
        G, robot = move(robot, V(0,-1), G)
    if m == '>':
        G, robot = move(robot, V(0,1), G)
    if m == 'v':
        G, robot = move2(robot, V(1,0), G)
    if m == '^':
        G, robot = move2(robot, V(-1,0), G)

print(score(G))