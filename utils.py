import math
from collections import defaultdict, deque
import copy
import numpy as np

## INPUT
def readlinesb(filename, prnt=False):
    with open(filename) as f:
        res = [l.rstrip('\n') for l in f.readlines()]
    if prnt:
        print(res[0])
    return res

def readlines(filename, prnt=False, sep=None, isstr=False, b=False):
    if b:
        return readlinesb(filename, prnt=prnt)
    with open(filename) as f:
        res = []
        res2 = []
        for l in f:
            if l == '\n':
                res2.append(res)
                res = []
            else:
                r = parseline(l, isstr, sep)
                res.append(r)
    res = res2 + [res] if res2 else res
    if len(res) == 1:
        res = res[0]
    if prnt:
        print(f"nlines: {len(res)}")
        print(res)
    return res

def parseline(l, isstr=False, sep=' '):
    if sep == -1:
        l = [x for x in l.rstrip('\n')]
    else:
        l = l.rstrip('\n').split(sep)
    r = []
    for x in l:
        r.append(parsestr(x, isstr))

    if len(l) == 1:
        return r[0]
    return r

def parsestr(x, isstr=False):
    if not isstr:
        if x.isnumeric():
            return int(x)
        try:
            x = float(x)
        except:
            return x
    return x

def ints(lines):
    return [int(x) for x in lines]

def inty(x):
    if type(x) != list:
        return int(x)
    return int(''.join(x))


## LOOPING
def ranger(x, f):
    r = []
    for i in range(len(x)):
        r2 = []
        for j in range(len(x[0])):
            r2.append(f(x[i][j]))
        r.append(r2)
    return r

def selfranger(x, f):
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = f(x[i][j])
    return x

def transpose(x):
    res = []
    for i in range(len(x[0])):
        nr = []
        for c in x:
            nr.append(c[i])
        res.append(nr)
    return res


## BINARY
def dec(x):
    x = inty(x)
    decimal, i = 0, 0
    while(x != 0):
        dec = x % 10
        decimal = decimal + dec * pow(2, i)
        x = x//10
        i += 1
    return decimal

def binflip(x):
    return ''.join('1' if a == '0' else '0' for a in x)


## MATRIX
class M():
    def __init__(self, inp):
        if type(inp[0]) == str:
            inp = [[parsestr(x) for x in r] for r in inp]
        self.G = inp
        self.m = len(self.G)
        self.n = len(self.G[0])

    def _check_oob(self, p):
        if p[0] < 0 or p[0] >= self.m or p[1] < 0 or p[1] >= self.n:
            return False
        return True

    def __getitem__(self, p):
        if type(p) == int:
            if self._check_oob((p,0)):
                return self.G[p]
            return self.G[p]
        if self._check_oob(p):
            return self.G[p[0]][p[1]]

    def __setitem__(self, p, v):
        if self._check_oob(p):
            self.G[p[0]][p[1]] = v

    def __iter__(self):
        for j in range(self.n):
            for i in range(self.m):
                yield V(i,j), self.G[i][j]

    def __str__(self):
        return '\n'.join([''.join([str(x) for x in r]) for r in self.G])

    def __add__(self, other):
        return M([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])

    def rotate(self):
        self.G = list(zip(*self.G[::-1]))

    def flipud(self):
        self.G = self.G[::-1]

    def fliplr(self):
        self.G = [r[::-1] for r in self.G]

    def step(self, p):
        return (p[0]+self.D[0], p[1]+self.D[1])

    def bfs(self, p, stepcond=None, rescond=None, diag=False, cangoback=False):
        if not stepcond:
            stepcond = lambda x: True
        if not rescond:
            rescond = lambda x: None
        q = deque([p])
        seen = set()
        res = []
        while q:
            for _ in range(len(q)):
                p = q.popleft()
                for np in p.steps(diag=diag):
                    if self[np] and np not in seen:
                        if stepcond(np,p):
                            if rescond(np,p):
                                res.append(np)
                            q.append(np)
                        if cangoback:
                            seen.add(np)
        return res


class V():
    def __init__(self, x, y):
        self.x = int(x) if type(x) == str else x
        self.y = int(y) if type(y) == str else y

    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y

    def __setitem__(self, i, v):
        if i == 0:
            self.x = v
        if i == 1:
            self.y = v

    def __add__(self, other):
        return V(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return V(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, V):
            return V(self.x * other.x, self.y * other.y)
        return V(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, V):
            return V(self.x / other.x, self.y / other.y)
        return V(self.x / other, self.y / other)

    def __floordiv__(self, other):
        if isinstance(other, V):
            return V(self.x // other.x, self.y // other.y)
        return V(self.x // other, self.y // other)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        yield self.x
        yield

    def __len__(self):
        return 2

    def d(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def steps(self, diag=False, included=False):
        dirs = [V(0,1),V(1,0),V(0,-1),V(-1,0)]
        if diag:
            dirs += [V(1,1),V(-1,1),V(1,-1),V(-1,-1)]
        for d in dirs:
            if included:
                yield self + d, d
            else:
                yield self + d

def dijkstras(G, start, end):
    q = [(0, start)]
    seen = set()
    while q:
        d, p = q.pop(0)
        if p == end:
            return d
        if p in seen:
            continue
        seen.add(p)
        for np in G[p]:
            q.append((d+G[p][np], np))
        q.sort()