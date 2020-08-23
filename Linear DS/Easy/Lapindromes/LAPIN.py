"""
Problem link: https://www.codechef.com/problems/LAPIN
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')



def solve():
    s = input()
    n = len(s)
    count_left = {}
    count_right = {}
    yes = 'YES'
    no = 'NO'
    for i in range(n//2):
        if s[i] not in count_left:
            count_left[s[i]] = 0 
        count_left[s[i]] += 1 
    if n%2:
        for i in range(n//2+1,n):
            if s[i] not in count_right:
                count_right[s[i]] = 0 
            count_right[s[i]] += 1 
    else:
        for i in range(n//2,n):
            if s[i] not in count_right:
                count_right[s[i]] = 0 
            count_right[s[i]] += 1 

    flag = True 
    for char in count_left:
        if char not in count_right:
            flag = False 
            break 
        elif count_right[char] != count_left[char]:
            flag = False 
            break
    if flag:
        print(yes)
    else:
        print(no)
        
if __name__ == '__main__':
    for t in range(int(input())):
        solve()
    