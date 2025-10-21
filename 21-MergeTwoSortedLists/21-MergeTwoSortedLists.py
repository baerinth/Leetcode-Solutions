# Last updated: 10/21/2025, 2:03:37 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        aList = ListNode(0)
        a = aList
        while list1 or list2:
            l1 = l2 = 101
            if list1: l1 = list1.val
            if list2: l2 = list2.val
            if l1<l2:
                newNode = ListNode(l1)
                list1=list1.next
            else:
                newNode = ListNode(l2)
                list2=list2.next
            a.next = newNode
            a = a.next
        return aList.next
                