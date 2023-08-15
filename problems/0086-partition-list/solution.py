# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:

        def iter_ll(head: ListNode | None) -> Iterator[ListNode]:
            while (t := head): head = head.next; yield t
        
        def allot(lls, node):
            k = node.val >= x
            lls[k].next = lls[k] = node
            return lls
        
        lt_head, ge_head = ListNode(), ListNode()
        lt_tail, ge_tail = reduce(allot, iter_ll(head), [lt_head, ge_head])

        lt_tail.next, ge_tail.next = ge_head.next, None
        return lt_head.next

