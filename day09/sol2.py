from utils import *

with open('day09/input.txt') as f:
    lines = [int(x) for l in f.readlines() for x in l.rstrip('\n')]
# with open('day09/test.txt') as f:
#     lines = [int(x) for l in f.readlines() for x in l.rstrip('\n')]

def sum_n(a, b):
    return (b-a+1)*(a+b)//2

idxs = []
b = 0
for i in range(len(lines)):
    idxs.append(b)
    b += lines[i]

res = 0
id = len(lines)//2
for j in range(len(lines)-1,-1,-2):
    fsize = lines[j]
    for i in range(1, j, 2):
        if lines[i] >= fsize:
            b = idxs[i]
            res += sum_n(b, b+fsize-1)*id
            idxs[i] += fsize
            lines[i] -= fsize
            break
    else:
        b = idxs[j]
        res += sum_n(b, b+fsize-1)*id
    id -= 1

print(res)
