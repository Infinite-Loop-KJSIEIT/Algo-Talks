"""
Problem link: https://www.hackerrank.com/challenges/largest-rectangle/problem
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')
from collections import Counter
import math
import os
import random
import re
import sys




"""
(6 - 4 - 1)*4  = 1*4 = 8
(6 - 3 - 1)*4  = 2*4 = 8 
(6 - 2 - 1)*4  = 3*4 = 12 


h =   [ 1, 2, 3, 4, 4, 4, 3, 1 ]
        0  1  2  3  4  5  6  7  8 

4 4 4 4 4 4 4 3

maxarea = 0 
"""






# Complete the largestRectangle function below.




# Time complexity : O(n^2) 
def brutforce(h):
    n = len(h)
    maxArea = 0
    for i in range(n):
        area = h[i]
        for j in range(i-1, -1, -1):
            if h[j] >= h[i]:
                area += h[i]
            else:
                break 
        for j in range(i+1, n):
            if h[j] >= h[i]:
                area += h[i]
            else:
                break 
        maxArea = max(area, maxArea)
    return maxArea



def largestRectangle(h):
    n = len(h)
    stack = [-1]
    maxArea = -float('inf')
    area = 0 
    i = 0
    while i < n:
        if stack[-1] == -1 or h[i] >= stack[-1]:
            stack.append(i)
            i += 1
        else:
            element = stack.pop()
            area = h[element]*(i - stack[-1] - 1)
            maxArea = max(area, maxArea)

    while stack[-1] != -1:
        element = stack.pop()
        area = h[element]*(n - stack[-1] -)
        maxArea = max(area, maxArea)
    
    return maxArea







def solve():
    n = int(input())
    h = list(map(int, input().split()))
    # print(largestRectangle(h))
    print(brutforce(h))

    
 
if __name__ == '__main__':
    solve()