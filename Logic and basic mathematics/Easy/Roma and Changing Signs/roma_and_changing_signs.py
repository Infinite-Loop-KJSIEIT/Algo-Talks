"""
Problem link:   https://codeforces.com/contest/262/problem/B
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        if a[i] < 0 and k:
            a[i] *=-1 
            k -= 1 
        else:
            break 

    if k%2:
        m = float('inf')
        index = -1 
        for i in range(n):
            if a[i] < m:
                m = a[i]
                index = i 
        a[index] *= -1 
    
    
            



    s = sum(a)
    print(s)
        
            



if __name__ == '__main__':
    solve()
    