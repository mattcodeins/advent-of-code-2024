from utils import *

inp = readlines('day13/input.txt')
# inp = readlines('day13/test.txt', prnt=True)

# 3 for A, 1 for B
# right (x), forward (y)

def solve(p2=False):
    eqs = []
    for l in inp:
        a1 = int(l[0][2][2:-1])
        a2 = int(l[0][3][2:])
        b1 = int(l[1][2][2:-1])
        b2 = int(l[1][3][2:])
        x = int(l[2][1][2:-1])
        y = int(l[2][2][2:])
        if p2:
            x += 10000000000000
            y += 10000000000000
        eqs.append((a1, a2, b1, b2, x, y))

    cost = 0
    for e in eqs:
        a1, a2, b1, b2, x, y = e
        A = np.array([[a1, b1], [a2, b2]])
        B = np.array([x, y])
        X = np.linalg.solve(A, B)
        if abs(X[0]-np.round(X[0])) < 1e-2 and abs(X[1]-np.round(X[1])) < 1e-2:
            cost += X[0]*3 + X[1]
    return round(cost)

print(solve())
print(solve(True))