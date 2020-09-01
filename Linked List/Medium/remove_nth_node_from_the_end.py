"""
Link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Solution by Keshav Mishra
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = 

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None and n ==1:
            return
        front, back = head, head 
        c = 1 
        while c != n:
            back = back.next 
            c += 1 
        prev = None 
        while back.next:
            prev = front 
            back , front = back.next , front.next 
        if prev is None:
            return head.next 
        prev.next = front.next 
        return head

             
            

        