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
        
