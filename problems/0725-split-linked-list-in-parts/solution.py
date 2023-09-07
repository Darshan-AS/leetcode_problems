# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        def lenLL(ll):
            n = 0
            while ll: n += 1; ll = ll.next
            return n
        
        def foo(ll, x):
            ll = ListNode(next=ll)
            while ll and x:
                ll = ll.next
                x -= 1
            t = ll.next
            ll.next = None
            return t

        n = lenLL(head)
        q, r = divmod(n, k)
        xs = chain(repeat(q + 1, r), repeat(q, k - r))
        zs = islice(accumulate(xs, foo, initial=head), k) if n else repeat(None, k)
        return list(zs)
        
