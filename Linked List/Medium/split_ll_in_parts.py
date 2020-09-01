"""
Link : https://leetcode.com/problems/split-linked-list-in-parts/
Solution by Keshav Mishra
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0 
        current = root 
        while current:
            n += 1 
            current = current.next 
        l = n//k 
        r = n%k 
        nodes = []
        current = root 
        for i in range(k):
            head = current 
            nodes.append(head)
            for j in range(l - 1 + (i < r)):
                if current:
                    current = current.next 
                else:
                    break 
            next = None 
            if current:
                next = current.next 
                current.next = None 
                current = next 
        return nodes
