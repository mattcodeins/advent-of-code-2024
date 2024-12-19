from utils import *

inp = readlines('day19/input.txt')
# inp = readlines('day19/test.txt', prnt=True)

patterns = [x.strip(',') for x in inp[0][0]]
designs = inp[1]

p1 = 0
p2 = 0
for d in designs:
    dp = [0 for _ in range(len(d)+1)]
    dp[0] = 1
    for i, x in enumerate(dp):
        if not(dp[i]):
            continue
        for p in patterns:
            if d[i:i+len(p)] == p:
                dp[i+len(p)] += dp[i]
    p1 += bool(dp[-1])
    p2 += dp[-1]

print(p1)
print(p2)