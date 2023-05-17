# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        LL = ListNode | None

        def iter_ll(ll: LL) -> Iterator[ListNode]:
            while ll: yield ll; ll = ll.next

        def last(ll: LL) -> ListNode:
            while ll and ll.next: ll = ll.next
            return ll
        
        def reverse(ll: LL) -> LL:
            a, b = None, ll
            while b: b.next, a, b = a, b, b.next
            return a

        def halves(ll: LL) -> tuple[LL, LL]:
            a = b = p = ListNode(next=ll)
            while p and p.next: b, p = b.next, p.next.next
            a, b.next, b = a.next, None, b.next
            return a, b
        
        def join(ll1: LL, ll2: LL) -> LL:
            last(ll1).next = ll2
            return ll1
        
        
        first, second = halves(head)
        second = reverse(second)
        max_twin_sum = max(map(lambda a, b: a.val + b.val, iter_ll(first), iter_ll(second)))
        second = reverse(second)
        head = join(first, second)

        return max_twin_sum
