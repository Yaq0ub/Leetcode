# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow, fast, and prev pointers to traverse the list
        slow, fast, prev = head, head, None
        
        # If the list is empty or has only one element, return None
        if not head or not head.next:
            return None

        # Traverse the list with two pointers:
        # 'slow' moves one step at a time,
        # 'fast' moves two steps at a time.
        while fast and fast.next:
            prev = slow          # 'prev' tracks the node before 'slow'
            slow = slow.next     # 'slow' moves to the next node
            fast = fast.next.next # 'fast' moves two nodes ahead
            
        # 'slow' is now at the middle node. 'prev' is the node before 'slow'.
        # Remove the middle node by linking 'prev.next' to 'slow.next'
        prev.next = slow.next
        
        # Return the head of the modified list
        return head
