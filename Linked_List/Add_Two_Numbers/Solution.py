# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, dummyHead, p, q = 0, ListNode(0), l1, l2
        curr = dummyHead
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next