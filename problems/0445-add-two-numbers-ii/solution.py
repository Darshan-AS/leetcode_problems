# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_int(ll: ListNode):
            n = 0
            while ll:
                n = n * 10 + ll.val
                ll = ll.next
            return n
        
        def to_linkedlist(n: int):
            ll = None
            while n:
                n, val = divmod(n, 10)
                node = ListNode(val)
                node.next = ll
                ll = node
            return ll if ll else ListNode(n)
        
        return to_linkedlist(to_int(l1) + to_int(l2))
        
        
