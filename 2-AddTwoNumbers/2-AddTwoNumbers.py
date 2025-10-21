# Last updated: 10/21/2025, 2:03:48 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        aList = ListNode(0)
        a = aList
        c = 0
        while l1 or l2:
            val1, val2 = 0,0
            if l1: 
                val1=l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            newNode = ListNode((val1+val2+c)%10)
            a.next = newNode
            a = a.next
            c=((val1+val2+c)//10)
        if c != 0: 
            newNode = ListNode((c)%10)
            a.next = newNode
            a = a.next
        return aList.next

