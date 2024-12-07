import math
from collections import defaultdict, deque
import copy
import time

## INPUT
def readlinesb(filename, prnt=False):
    with open(filename) as f:
        res = [l.rstrip('\n') for l in f.readlines()]
    if prnt:
        print(res[0])
    return res

def readlines(filename, isstr=False, sep=None, prnt=True, b=False):
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
        if res2:
            res2.append(res)
            return res2
    if prnt:
        print(res[0])
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


## GRID
class Grid():
    def __init__(
            self,
            grid:list[list[any]]=None,
            start=(0,0),
            dir=0,
        ):
        self.G = grid
        if type(start) != tuple:
            for i, r in enumerate(self.G):
                for j, x in enumerate(r):
                    if x == start:
                        start = (i,j)
                        break
        self.X = start
        self.D = dir
        super().__init__()

    def __getitem__(self, p):
        return self.G[p[0]][p[1]]

    def __setitem__(self, p, v):
        self.G[p] = v

    def __str__(self):
        return '\n'.join([''.join([str(x) for x in r]) for r in self.G])

    def rotate(self):
        self.G = list(zip(*self.G[::-1]))

    def step(self, p):
        return (p[0]+self.D[0], p[1]+self.D[1])
