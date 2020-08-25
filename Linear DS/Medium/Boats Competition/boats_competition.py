import sys

def uno(): return int(sys.stdin.readline().strip())
def dos(): return sys.stdin.readline().strip()
def tres(): return map(int, sys.stdin.readline().strip().split())
def cuatro(): return sys.stdin.readline().strip().split()

for _ in range(uno()):
    n = uno()
    w = list(tres())
    d, m = {}, 0
    for i in w:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in range(2, 2*n+1):
        d1, l = d.copy(), 0
        for j in range(n):
            if w[j] in d1 and i-w[j] in d1:
                if w[j] != i-w[j] and (d1[w[j]] > 0 and d1[i-w[j]] > 0):
                    l += 1
                    d1[w[j]] -= 1
                    d1[i-w[j]] -= 1
                elif w[j] == i-w[j] and d1[w[j]] > 1:
                    l += 1
                    d1[w[j]] -= 2
        m = max(l, m)
    print(m)
