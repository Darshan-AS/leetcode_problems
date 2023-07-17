# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_int(ll: ListNode) -> int:
            n = 0
            while ll: n = n * 10 + ll.val; ll = ll.next
            return n
        
        def to_LL(n: int) -> ListNode:
            ll = None
            while n: n, val = divmod(n, 10); ll = ListNode(val, ll)
            return ll or ListNode()
        
        return to_LL(to_int(l1) + to_int(l2))
