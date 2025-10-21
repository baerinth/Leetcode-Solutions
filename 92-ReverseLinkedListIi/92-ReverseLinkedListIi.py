# Last updated: 10/21/2025, 2:03:26 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        aList = head
        for x in range(left-1):
            if head.next: head = head.next
        while left < right:
            inc = head
            for x in range(right-left):
                inc = inc.next
            head.val, inc.val = inc.val, head.val
            head = head.next
            left += 1
            right -= 1
        return aList

    
        
            