from utils import *

inp = readlines('day11/input.txt', isstr=True)
# inp = readlines('day11/test.txt', isstr=True)

def solve(blinks):
    stones = defaultdict(int) | {s:1 for s in inp}
    for _ in range(blinks):
        newstones = defaultdict(int)
        for s,c in stones.items():
            if s == '0':
                newstones['1'] += c
            elif len(s) % 2 == 0:
                s1,s2 = s[:len(s)//2], s[len(s)//2:]
                newstones[s1] += c
                newstones[s2] += c
            else:
                newstones[str(int(s)*2024)] += c
        stones = newstones
    return sum(newstones.values())

print(solve(25))
print(solve(75))