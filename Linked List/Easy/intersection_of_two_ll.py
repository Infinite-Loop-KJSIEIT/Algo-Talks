"""
Problem link: https://leetcode.com/problems/intersection-of-two-linked-lists/
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







def intersection(head1,head2):
    pass 

    







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
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1 = 0 
        n2 = 0 
        current = headA 
        while current:
            n1 += 1 
            current = current.next 
        current = headB 
        while current:
            n2 += 1 
            current = current.next 
        iter1 = headA 
        iter2 = headB 
        if n1 > n2:
            k = n1 - n2 
            while k:
                k -= 1 
                iter1 = iter1.next
        elif n2 > n1:
            k = n2 - n1 
            while k:
                k -= 1
                iter2 = iter2.next 
        while iter1 and iter2:
            if iter1 is iter2:
                return iter1 
            iter1 = iter1.next 
            iter2 = iter2.next 
        return None 
        
     


    

    
    

def intersection(head1, head2):
    if head1 is None or head2 is None:
        return
    n1 = 0 
    curr = head1 
    while curr:
        n1 +=1 
        curr = curr.next 
    n2 = 0 
    curr = head2
    while curr:
        n2 +=1 
        curr = curr.next 
    k = abs(n1-n2)
    if n1 > n2:
        while k:
            head1 = head1.next 
            k -= 1
    else:
        while k:
            head2 = head2.next 
    
    while head1 and head2:
        if head1 == head2:
            return head1 
        head1 = head1.next 
        head2 = head2.next 
    return None 
    


    