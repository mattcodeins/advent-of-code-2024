from utils import *
import re

lines = readlines('day03/input.txt', b=True, prnt=False)
# lines = readlines('day03/test.txt')

def solve(p2=False):
    res = 0
    on = True
    for l in lines:
        regx = r'mul\(\d*,\d*\)|do\(\)|don\'t\(\)' if p2 else r'mul\(\d*,\d*\)'
        sols = re.findall(regx, l)
        for s in sols:
            if s == "do()":
                on = True
            elif s == "don't()":
                on = False
            elif on:
                a, b = s.split(",")
                a, b = int(a[4:]), int(b[:-1])
                res += a*b
    return res

print(solve())
print(solve(True))