"""
Problem link: https://leetcode.com/problems/add-two-numbers/
Solution By Keshav Mishra 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getSum(a,b,c = 0):
            ans = a + b + c
            if ans > 9:
                ans = str(ans)
                return int(ans[-1]), int(ans[:-1])
            return ans, 0
        s = 0 
        c1, c2 = l1, l2
        c3 = ListNode(-1)
        head = c3 
        a ,b = 0 ,0
        while c1 and c2:
            c3.next = ListNode(-1)
            c3 = c3.next 
            a,b = getSum(c1.val, c2.val,b)
            c3.val = a  
            c1 = c1.next 
            c2 = c2.next 
        if c1:
            while c1:
                a,b = getSum(c1.val,b)
                c3.next = ListNode(a)
                c1 = c1.next 
                c3 = c3.next  
        elif c2:
            while c2:
                a,b = getSum(c2.val,b)
                c3.next = ListNode(a)
                c2 = c2.next 
                c3 = c3.next  
        if b:
            n = str(b).split()
            for i in reversed(n):
                c3.next = ListNode(int(i))
                c3 = c3.next 
        c3 = head 
        
        return head.next  








            