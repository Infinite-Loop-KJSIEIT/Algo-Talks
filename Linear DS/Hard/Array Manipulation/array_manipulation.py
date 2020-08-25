import sys

def uno(): return int(sys.stdin.readline().strip())
def dos(): return sys.stdin.readline().strip()
def tres(): return map(int, sys.stdin.readline().strip().split())
def cuatro(): return sys.stdin.readline().strip().split()

n, m = tres()
ar, mx, sm = [0]*(n+1), 0, 0
for i in range(m):
    a, b, k = tres()
    ar[a-1] += k
    ar[b] -= k
for i in range(n+1):
    sm += ar[i]
    mx = max(mx, sm)
print(mx)
