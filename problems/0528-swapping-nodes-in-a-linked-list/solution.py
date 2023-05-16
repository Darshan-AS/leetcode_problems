# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode | None, k: int) -> ListNode | None:
        
        def iter_ll(ll: ListNode | None) -> Iterable[ListNode]:
            while ll: yield ll; ll = ll.next
        
        T = TypeVar('T')
        def last(xs: Iterable[T]) -> T:
            return reduce(lambda _, x: x, xs)
        
        sentinal_head = ListNode(next=head)
        xs, ys = iter_ll(sentinal_head), iter_ll(sentinal_head)

        k_begin = next(islice(ys, k - 1, None))
        k_end = last(zip(xs, ys))[0]

        b, e = k_begin.next, k_end.next
        k_begin.next, k_end.next = e, b
        b.next, e.next = e.next, b.next
        
        return sentinal_head.next
