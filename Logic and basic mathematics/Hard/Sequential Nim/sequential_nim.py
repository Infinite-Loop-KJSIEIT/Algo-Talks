"""
Problem link: https://codeforces.com/problemset/problem/1382/B
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    first = 'First'
    second = 'Second'
    ones = 0
    for i in range(n):
        if a[i] !=1:
            break 
        ones += 1
    if i%2==1:
        winner = second
    else:
        winner = first
    print(winner)


if __name__ == '__main__':
    for t in range(int(input())):
        solve()