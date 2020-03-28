# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_node = p3 = ListNode(0)
        p1, p2 = l1, l2
        
        carry = 0
        while p1 or p2:
            s = carry
            if p1:
                s += p1.val
                p1 = p1.next
            
            if p2:
                s += p2.val
                p2 = p2.next
                
            p3.next = ListNode(s % 10)
            carry = s // 10
            p3 = p3.next
        
        if carry:
            p3.next = ListNode(carry)
        
        return sum_node.next
