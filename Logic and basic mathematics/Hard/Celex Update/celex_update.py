"""
Problem link:   https://codeforces.com/contest/1358/problem/C
"""

from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    x1, y1, x2, y2 = map(int, input().split())
    print((x2 - x1) * (y2 - y1) + 1)


if __name__ == '__main__':
    for t in range(int(input())):
        solve()
    