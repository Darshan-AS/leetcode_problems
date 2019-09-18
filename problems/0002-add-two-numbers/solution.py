# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = result = ListNode(0)
        
        sum, carry = 0, 0
        p, q = l1, l2
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            
            sum = (x + y + carry)
            carry = sum // 10

            result.next = ListNode(sum % 10)
            result = result.next
            p = p.next if p else None
            q = q.next if q else None
        
        if carry:
            result.next = ListNode(1)
            
        return l3.next
