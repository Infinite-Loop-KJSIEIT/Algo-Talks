#solution by Vedant Kokate
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
t=int(input())
for T in range(t):
    n,x=get_ints()
    if n==1:
        print(0)
    elif n==2:
        print(x)
    else:
        print(x*2)
