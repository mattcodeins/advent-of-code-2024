from utils import *

inp, size = readlines('day14/input.txt'), V(101, 103)
# inp, size = readlines('day14/test.txt', prnt=True), V(11,7)

guards = []
for p,v in inp:
    p = V(*p[2:].split(','))
    v = V(*v[2:].split(','))
    guards.append((p,v))

newguards = []
for g in guards:
    p,v = g
    p.x = (p.x + v.x*100) % size.x
    p.y = (p.y + v.y*100) % size.y
    newguards.append(p)

quads = [0 for _ in range(4)]
for g in newguards:
    if g.x < size.x//2 and g.y < size.y//2:
        quads[0] += 1
    elif g.x > size.x//2 and g.y < size.y//2:
        quads[1] += 1
    elif g.x < size.x//2 and g.y > size.y//2:
        quads[2] += 1
    elif g.x > size.x//2 and g.y > size.y//2:
        quads[3] += 1
print(math.prod(quads))