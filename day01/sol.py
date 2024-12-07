from utils import *

lines = readlines('day01/input.txt', prnt=False)
# lines = readlines('day071test.txt')
# print(lines[0])

x = [a[0] for a in lines]
y = [a[1] for a in lines]
x.sort()
y.sort()

t = 0
for i in range(len(x)):
    t += abs(x[i]-y[i])
print(t)

t = 0
for a in x:
    t += a * sum([b == a for b in y])

print(t)