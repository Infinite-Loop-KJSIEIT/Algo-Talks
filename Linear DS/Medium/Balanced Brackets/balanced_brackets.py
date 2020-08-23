"""
Problem link: https://www.hackerrank.com/challenges/balanced-brackets/problem
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')

# Constants 
YES = 'YES'
NO = 'NO'
yes = 'yes'
no = 'no'
true = 'true'
false = 'false'

def isMatching(a,b):
    if a == '[' and b == ']':
        return True 
    elif a == '{' and b == '}':
        return True 
    elif a == '(' and b == ')':
        return True 
    else:
        return False 


def solve():
    s = input()
    stack = []
    
    flag = True 
    
    for char in s:
        if char in "{[(":
            stack.append(char)
        elif len(stack) == 0:
            flag = False 
            break 
        else:
            element = stack.pop()
            if isMatching(element, char):
                continue 
            else:
                flag = False 
                break 
            
    if len(stack):
        return NO 
    if flag:
        return YES
    else:
        return NO

if __name__ == '__main__':
    for t in range(int(input())):
        print(solve())
    