"""
Problem link: https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
from collections import Counter , deque
from queue import PriorityQueue
import math


helperConstants = True 
helperUtilityFunctions = True 

def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')
if helperConstants:
    YES = 'YES'
    NO = 'NO'
    yes = 'yes'
    no = 'no'
    true = 'true'
    false = 'false'
    FALSE = 'FALSE'
    TRUE = 'TRUE'
    IMPOSSIBLE = 'IMPOSSIBLE'
    POSSIBLE = 'POSSIBLE'
    INF = float('inf')

if helperUtilityFunctions:
    # Input utility functions
    def getInputArray():
        return list(map(int, input().split()))
    def getIntegerInputs():
        return map(int, input().split())
    def getInputIntegerMatrix(n):
        matrix = []
        for i in range(n):
            matrix.append(list(map(int,input().split())))
        return matrix
    def getInputStringMatrix(n):
        matrix = []
        for i in range(n):
            matrix.append(input())
        return matrix

    # Output Utility functions
    def outputIntegerMatrix(matrix):
        for i in range(len(matrix)):
            print(*matrix[i])
    def outputStringMatrix(matrix):
        for i in range(len(matrix)):
            print(matrix[i])
    def kickstartoutput(testcase,*outputs):
        print('Case #%d:'%(testcase), *outputs)
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getLLInput():
    n = int(input())
    head = None 
    for i in range(n):
        val = int(input())
        if head:
            current.next = ListNode(val = val)
            current = current.next 
        else:
            head = ListNode(val = val)
            current = head 
    return head 

def printLL(head):
    while head:
        print(head.val, end = '->')
    print(None)

def removeDuplicates(head):
    if head is None:
        return head 
    prev = None 
    current = head 
    while current:
        if prev:
            if prev.data != current.data:
                prev.next = current
                prev = current  
        else:
            prev = current 
        current = current.next 
    prev.next = None 
    return head
    
if __name__ == '__main__':
    
    removeDuplicates()