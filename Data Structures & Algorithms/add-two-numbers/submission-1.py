# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        dummy = result
        remainder = 0

        while l1 and l2:
            total = l1.val + l2.val + remainder
            value = total % 10 
            remainder = total // 10
            dummy.next = ListNode(value)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                total = l1.val + remainder
                value = total % 10 
                remainder = total // 10
                dummy.next = ListNode(value)
                dummy = dummy.next
                l1 = l1.next
        elif l2:
            while l2:
                value = (l2.val + remainder) % 10 
                remainder = (l2.val + remainder) // 10
                dummy.next = ListNode(value)
                dummy = dummy.next
                l2 = l2.next

        if remainder > 0:
            dummy.next = ListNode(remainder)
        return result.next