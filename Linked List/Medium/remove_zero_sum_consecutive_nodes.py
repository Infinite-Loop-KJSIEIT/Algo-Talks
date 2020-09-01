"""
Link:https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
Solution by Keshav Mishra
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        ptr = ListNode(-1)
        ptr.next = head 
        current = head 
        head = ptr 
        while head:
            s = 0 
            while current:
                s += current.val 
                if s == 0:
                    head.next = current.next 
            
                current = current.next 
            head = head.next 
            if head:
                current = head.next 
    
        return ptr.next 
         

            