from utils import *

inp = readlines('day15/input.txt')
# inp = readlines('day15/test.txt')

G = M(inp[0])
moves = ''.join(inp[1])

for i, x in G:
    if x == '@':
        robot = i
        break

def score(G):
    r = 0
    for i, x in G:
        if x == 'O':
            r += i.x*100 + i.y
    return r 

def move(i, d, G):
    j = i+d
    x = 0
    while G[j] == 'O':
        x += 1
        j = j+d
    if G[j] == '#':
        return G, i
    if G[j] == '.':
        for _ in range(x):
            G[j] = 'O'
            j -= d
        G[j] = '@'
        G[i] = '.'
        return G, j


for m in moves:
    if m == '<':
        G, robot = move(robot, V(0,-1), G)
    if m == '>':
        G, robot = move(robot, V(0,1), G)
    if m == 'v':
        G, robot = move(robot, V(1,0), G)
    if m == '^':
        G, robot = move(robot, V(-1,0), G)

print(score(G))
