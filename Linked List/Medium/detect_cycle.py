# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Link : https://leetcode.com/problems/linked-list-cycle-ii/
Solution by Keshav Mishra
"""
# Approach 1 
# O(N) - Space 
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hashmap = set()
        node = head 
        while node:
            if node is None:
                return None 
            elif node in hashmap:
                return node 
            else:
                hashmap.add(node)
            node = node.next 

def detect(head):
    if head is None:
        return 
    hashmap = set()
    curr = head 
    while curr:
        if curr in hashmap:
            return curr
        hashmap.add(curr)
    return None 

def detect(head):
    if head is None:
        return
    slow = head 
    fast = head 
    flag = None 
    while fast and fast.next :
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            flag = fast 
            break 
        
    if flag:
        return 
    iter1 = head 
    iter2 = flag
    while iter1 and iter2:
        if iter1 is iter2:
            return iter1 
        iter1 = iter1.next 
        iter2 = iter2.next 




        















# Approach 2 
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def helper(head):
            if head is None or head.next is None:
                return None 
            slow = head 
            fast = head
            while fast and fast.next:
                slow = slow.next 
                fast = fast.next.next 
                if slow is fast:
                    return slow 
        
        fast = helper(head)
        if fast is None:
            return None 
        
        slow = head 
        while fast is not slow:
            fast = fast.next 
            slow = slow.next 
        
        return slow 
        

        



     
        