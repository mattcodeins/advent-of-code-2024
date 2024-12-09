from utils import *

lines = readlines('day02/input.txt')
# lines = readlines('day02/test.txt')

def solve(p2=False):
    safe = 0
    for l in lines:
        inc = l[1] > l[0]
        b = None
        bad = True
        for x in l:
            if b and (abs(x-b) > 3 or inc and b >=x or not inc and b <= x):
                if p2 and bad:
                    bad = False
                    b = x
                    continue
                else:
                    break
            b = x
        else:
            safe += 1
    return safe

print(solve())
print(solve(True))