from utils import *

inp = readlines('day17/input.txt')
# inp = readlines('day17/test.txt')

rs = []
for x in inp[0]:
    rs.append(x[2])
print(rs)

ops = [int(x) for x in inp[1][0][1].split(',')]
print(ops)

def getcombo(o):
    if o in [0,1,2,3]:
        return o
    if o == 4:
        return rs[0]
    if o == 5:
        return rs[1]
    if o == 6:
        return rs[2]

i = 0
out = []
while i < len(ops)-1:
    ins = ops[i]
    op = ops[i+1]
    print(ins, op)
    if ins == 0:
        rs[0] //= 2**getcombo(op)
    if ins == 1:
        rs[1] ^= op
    if ins == 2:
        rs[1] = getcombo(op)%8
    if ins == 3:
        if rs[0] != 0:
            i = op
            continue
    if ins == 4:
        rs[1] ^= rs[2]
    if ins == 5:
        out.append(str(getcombo(op)%8))
    if ins == 6:
        rs[1] = rs[0] // 2**getcombo(op)
    if ins == 7:
        rs[2] = rs[0] // 2**getcombo(op)
    print(i, rs)
    i += 2

print(','.join(out))