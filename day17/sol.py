from utils import *

inp = readlines('day17/input.txt')
# inp = readlines('day17/test.txt')

inA = inp[0][0][2]
ops = [int(x) for x in inp[1][0][1].split(',')]

def getcombo(o, rs):
    if o in [0,1,2,3]:
        return o
    if o == 4:
        return rs[0]
    if o == 5:
        return rs[1]
    if o == 6:
        return rs[2]

def runsim(A, ops=ops, early=False):
    i = 0
    out = []
    rs = [A, 0, 0]
    while i < len(ops)-1:
        ins = ops[i]
        op = ops[i+1]
        # print(ins, op)
        if ins == 0:
            rs[0] //= 2**getcombo(op, rs)
        if ins == 1:
            rs[1] ^= op
        if ins == 2:
            rs[1] = getcombo(op, rs)%8
        if ins == 3:
            if rs[0] != 0:
                i = op
                continue
        if ins == 4:
            rs[1] ^= rs[2]
        if ins == 5:
            x = getcombo(op, rs)%8
            if early:
                return x
            out.append(str(x))
        if ins == 6:
            rs[1] = rs[0] // 2**getcombo(op, rs)
        if ins == 7:
            rs[2] = rs[0] // 2**getcombo(op, rs)
        # print(i, rs)
        i += 2
    return ','.join(out)

def findinvs(ops=ops, add=0, find=-1):
    invs = []
    for x in range(8):
        y = runsim(x+add, ops, True)
        if find == y:
            invs.append(x)
    return invs

print(runsim(inA, ops))

q = deque([0])
for o in reversed(ops):
    for _ in range(len(q)):
        x = 8*q.popleft()
        invs = findinvs(ops, x, o)
        for i in invs:
            if x+i not in q:
                q.append(x+i)

q = sorted(q)
print(q[0])
# print(runsim(q[0], ops))