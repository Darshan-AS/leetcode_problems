# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        new_head = ListNode(next=head)

        left_end = reduce(lambda a, _: a.next, range(left - 1), new_head)
        
        curr_node, prev_node = reduce(
            lambda a, _: (a[0].next, setattr(a[0], 'next', a[1]) or a[0]),
            range(left, right + 1),
            (left_end.next, None),
        )
        
        left_end.next.next, left_end.next = curr_node, prev_node
        return new_head.next
        
