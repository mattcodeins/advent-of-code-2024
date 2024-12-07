from utils import *

lines = readlines('day04/input.txt', prnt=False)
# lines = readlines('day04/test.txt')

m, n = len(lines), len(lines[0])

t = 0
lets = ["X","M","A","S"]
for i in range(m):
    for j in range(n):
        if lines[i][j] == lets[0]:
            for d1 in [-1,0,1]:
                for d2 in [-1,0,1]:
                    for x in range(1,4):
                        a, b = i+d1*x, j+d2*x
                        if a >= m or a < 0 or b >= n or b < 0 or lines[a][b] != lets[x]:
                            break
                    else:
                        t += 1
print(t)

t = 0
for i in range(m):
    for j in range(n):
        if lines[i][j] == "A":
            criss = False
            for d1 in [-1, 1]:
                for d2 in [-1, 1]:
                    if i+d1 >= m or i+d1 < 0 or j+d2 >= n or j+d2 < 0:
                        continue
                    if lines[i+d1][j+d2] == "M":
                        a,b = i-d1, j-d2
                        if a >= m or a < 0 or b >= n or b < 0:
                            continue
                        if lines[a][b] == "S":
                            if not criss:
                                criss = True
                            else:
                                t += 1
print(t)