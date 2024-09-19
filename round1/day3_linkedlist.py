# LC203 Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/
'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        if not head:
            return None
        while cur.next is not None:
            if cur.next.val == val:
                # remove the node
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

# LC206 Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre