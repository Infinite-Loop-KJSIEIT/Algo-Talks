"""
Problem link: https://www.hackerrank.com/challenges/simple-text-editor/problem
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')



def solve():
    s = ''
    stack = []
    q = int(input())
    for i in range(q):
        k = input().split()
        if k[0] == '1':
            stack.append(s)
            s += k[1]
        elif k[0] == '2':
            stack.append(s)
            s = s[:len(s)-int(k[1])]
        elif k[0] == '3':
            print(s[int(k[1])-1])
        elif k[0] == '4':
            s = stack.pop()
 
if __name__ == '__main__':
    solve()