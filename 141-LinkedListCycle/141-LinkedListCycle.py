# Last updated: 10/21/2025, 2:03:21 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = {}
        while head:
            if cycle.get(head): return True
            else: cycle[head] = head.val
            head = head.next
        return False