

#solution by vedant kokate
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
alp=list(get_ints())
s=sys.stdin.readline()
M=0
for i in s:
    if alp[ord(i)-97]>M:
        M=alp[ord(i)-97]

print(len(s)*M)
        
