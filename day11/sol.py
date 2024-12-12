from utils import *

inp = readlines('day11/input.txt', True)
# inp = readlines('day11/test.txt', True)

def p1():
    stones = inp
    for _ in range(25):
        newstones = []
        for s in stones:
            if s == 0:
                newstones.append(1)
            elif len(str(s)) % 2 == 0:
                s1,s2 = str(s)[:len(str(s))//2], str(s)[len(str(s))//2:]
                newstones.append(int(s1))
                newstones.append(int(s2))
            else:
                newstones.append(s*2024)
        stones = newstones
    return len(newstones)

def p2():
    stones = {s:1 for s in inp}
    for _ in range(75):
        newstones = {}
        for s,c in stones.items():
            if s == 0:
                newstones[1] = newstones.get(1,0) + c
            elif len(str(s)) % 2 == 0:
                s1,s2 = str(s)[:len(str(s))//2], str(s)[len(str(s))//2:]
                newstones[int(s1)] = newstones.get(int(s1),0) + c
                newstones[int(s2)] = newstones.get(int(s2),0) + c
            else:
                newstones[s*2024] = newstones.get(s*2024,0) + c
        stones = newstones
    return sum(newstones.values())


print(p1())
print(p2())