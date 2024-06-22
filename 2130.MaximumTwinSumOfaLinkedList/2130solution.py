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
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Initialize slow, fast, and prev pointers to traverse the list
        slow, fast, prev = head, head, None
        
        # Reverse the first half of the linked list while finding the middle
        while fast and fast.next:
            fast = fast.next.next    # 'fast' moves two steps at a time
            tmp = slow.next          # Temporarily store the next node
            slow.next = prev         # Reverse the link
            prev = slow              # Move 'prev' to the current 'slow'
            slow = tmp               # Move 'slow' to the next node
        
        # Initialize result to store the maximum twin sum
        result = 0
        
        # Compare the values from the reversed first half and the second half
        while prev and slow:
            # Update the result with the maximum twin sum
            result = max(result, prev.val + slow.val)
            # Move to the next pair of nodes
            prev = prev.next
            slow = slow.next
        
        # Return the maximum twin sum
        return result
