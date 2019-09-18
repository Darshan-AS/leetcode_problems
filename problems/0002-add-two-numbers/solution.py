# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = result = ListNode(0)
        
        sum, carry = 0, 0
        while l1 and l2:
            sum = (l1.val + l2.val + carry) % 10
            
            node = ListNode(sum)
            carry = (l1.val + l2.val + carry) // 10
            
            result.next = node
            result = node
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            node = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            result.next = node
            result = node
            l1 = l1.next
            
        while l2:
            node = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            result.next = node
            result = node
            l2 = l2.next
        
        if carry:
            result.next = ListNode(1)
            
        return l3.next
