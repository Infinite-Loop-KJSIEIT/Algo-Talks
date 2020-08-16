"""
Problem link:  https://codeforces.com/contest/1355/problem/A
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    a, k = map(int, input().split())
    m1 = int(min(str(a)))
    m2 = int(max(str(a)))
    for i in range(k-1):
        if m1 == 0 or m2 == 0:
            break
        else:
            a += m1*m2
            m1 = int(min(str(a)))
            m2 = int(max(str(a)))
    print(a)



if __name__ == '__main__':
    for t in range(int(input())):
        solve()
