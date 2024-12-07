from utils import *

lines = readlines('day07/input.txt', sep=' ', prnt=False)
# lines = readlines('day07/test.txt', sep=' ')

newlines = []
for l in lines:
    newlines.append([int(l[0][:-1])] + l[1:])
lines = newlines
# print(lines[0])

def qloop(l, p2=False):
    tv = l[0]
    q = deque([l[1]])
    for i in range(2, len(l)):
        for _ in range(len(q)):
            x = q.popleft()
            eqs = [x+l[i],x*l[i]]
            if p2:
                eqs.append(int(str(x)+str(l[i])))
            for v in eqs:
                if v <= tv:
                    q.append(v)
    return tv if tv in q else 0

print(sum([qloop(l) for l in lines]))
print(sum([qloop(l, True) for l in lines]))
