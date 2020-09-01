"""
Link : https://leetcode.com/problems/copy-list-with-random-pointer/
Solution by Keshav Mishra 
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next = None, random = None, ll = None):
        self.val = int(x)
        self.next = next
        self.random = random
        self.ll = ll


#Approach 1 
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head 
        hashmap = dict()
        def helper(head):
            newHead = Node(-1)
            current = newHead
            while head:
                current.next = Node(head.val)
                hashmap[head] = current.next 
                head = head.next
                current = current.next 
            return newHead.next
        newHead = helper(head)
        current1 = newHead 
        current2 = head 
        while current1 and current2:
            current1.random = None if not current2.random else hashmap[current2.random]
            current1 = current1.next 
            current2 = current2.next 
        return newHead

# Approach 2 
class Solution:
    def copyRandomList(self, head) :
        def setRandom(node):
            return None if not node.random else node.random
        def setRandomPtr(node):
            if node.random is None:
                return None 
            return node.random.next  
        def printLL(head):
            while head:
                print(head.val, None if not head.random else str(head.random.val) +" "+ str(head.random.ll))
                head = head.next 
            # print(None)
        # printLL(head)
        if head is None:
            return

        def putNodesInBetween(head):
            current = head 
            while current:
                nextptr = current.next 
                newNode = Node(current.val, ll = 'du')
                current.next = newNode 
                newNode.next = nextptr
                current = nextptr 
        
        def setRandomPointers(head): 
            current = head 
            while current:
                current.next.random = None if not current.random else current.random.next
                current = current.next.next 
            # while current:
            #     nextptr = current.next
            #     nextptr.random = setRandomPtr(current)
            #     current = nextptr.next
                 
        
        def getClone(head):
             
            newHead = head.next 
            current = head 
            while current:
                node = current.next 
                current.next = current.next.next
                current = current.next  
                node.next = None if not current else current.next 
            return newHead 

        putNodesInBetween(head)
        print('-------')
        printLL(head)
        setRandomPointers(head)
        print('-------')
        printLL(head)
        clone =  getClone(head)
        print('-------')
        printLL(clone)
        return clone 

one = Node(1, ll = 'og')
two = Node(2,ll = 'og')
three = Node(3,ll = 'og')
four = Node(4,ll = 'og')
head = one 
one.next = two 
two.next = three
three.next = four 
one.random = four 
two.random = two 
three.random = one 

# one = Node(-1, ll = 'og')
# two = Node(0,ll = 'og')
# one.next = two 
# one.random = two
# two.random = one
# head = one
s1 = Solution()
s1.copyRandomList(head)




            


        