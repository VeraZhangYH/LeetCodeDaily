#LC24 Swap nodes in pairs: https://leetcode.com/problems/swap-nodes-in-pairs/description/
''''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
# Understand: swap every two adjacent nodes
# Match: create temp node and change the next pointer of the node
#        create a dummy node to return the new linked list
# Plan: create a dummy node to return the new linked list, and use the dummy node to iterate the linked list
#       iterate each two nodes and swap them
# draw the linked list to understand the process!
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next is not None and cur.next.next is not None:
            temp = cur.next
            temp1 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = temp
            temp.next = temp1
            cur = cur.next.next
        return dummy.next

#LC19 Remove Nth Node From End of List: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = self.findNthFromEnd(dummy, n+1)
        if p.next is not None:
            p.next = p.next.next
        return dummy.next

    def findNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        for i in range(0, n):
            if fast is not None:
                fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next 
        return slow
'''
for i in range(0, n):
            if fast is not None:
                fast = fast.next
==
while fast is not None:
    fast = fast.next
    n -= 1
    if n == 0:
        break
'''

# LC160 Intersection of Two Linked Lists: https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''
# Understand: find the intersection of two linked lists
# Match: two pointers
# Plan: create two pointers to iterate the two linked lists, if one pointer reaches the end of the linked list, then move it to the head of the other linked list
#       if the two pointers meet, then return the node
# Method 1
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1!= p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
# method 2
# Plan: calculate the length of the two linked lists, and then move the longer linked list to the same length as the shorter linked list
#      then iterate the two linked lists to find the intersection
#      if the two linked lists have no intersection, then the two pointers will meet at the end of the linked lists
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        cur = headA
        while cur is not None:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur is not None:
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:
            headA = self.moveforward(headA, lenA - lenB)
        else:
            headB = self.moveforward(headB, lenB-lenA)
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    # move the head forward for steps
    def moveforward(self, head: ListNode, steps: int) -> Optional[ListNode]:
        while steps > 0:
            head = head.next
            steps -= 1
        return head
    
# LC142 Linked List Cycle2: https://leetcode.com/problems/linked-list-cycle/
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
'''
# two pointers: fast and slow
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:     
                p1 = head
                p2 = fast
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1