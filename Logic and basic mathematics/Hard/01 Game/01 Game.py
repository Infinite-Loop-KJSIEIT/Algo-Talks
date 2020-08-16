

#solution by vedant kokate
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
n=int(input())
for i in range(n):
    s=input()
    one=s.count("1")
    zero=s.count("0")
    m=min(zero,one)
    if m%2==0:
        print("NET")
    else:
        print("DA")


        
