"""
Problem link: https://codeforces.com/contest/544/problem/B
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n, k = map(int, input().split())
    flag1 = False
    flag2 = False
    matrix = []
    for i in range(n):
        new = ""
        if k:
            if flag2:
                flag1 = False
                flag2 = False
            else:
                flag1 = True
                flag2 = True

        for j in range(n):
            if k:
                if flag1:
                    new += 'L'
                    flag1 = False
                    k -= 1 
                else:
                    new += 'S'
                    flag1 = True
            else:
                new += 'S'
        matrix.append(new)
    if k:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            print(matrix[i])





if __name__ == '__main__':
    
    solve()