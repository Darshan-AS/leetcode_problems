# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
MaybeLL = ListNode | None

class Solution:
    def reorderList(self, head_: MaybeLL) -> None:
        def split_in_half(head: MaybeLL) -> tuple[MaybeLL, MaybeLL]:
            i = j = ListNode(next=head)
            while j and j.next:
                i, j = i.next, j.next.next
                
            f_half, s_half = head, i.next
            i.next = None
            return f_half, s_half
        
        def reverse(head: MaybeLL) -> MaybeLL:
            i, j = None, head
            while j:
                j.next, i, j = i, j, j.next
            return i
        
        def unthreadLL(head: MaybeLL) -> Iterator[ListNode]:
            while head:
                node, head = head, head.next
                node.next = None
                yield node
        
        def threadLL(list_nodes: Iterator[ListNode]) -> MaybeLL:
            sentinal_head = i = ListNode()
            for node in list_nodes:
                i.next = node
                i = i.next
            return sentinal_head.next
        
        
        first_half, second_half = split_in_half(head_)
    
        nodes = list(chain.from_iterable(zip_longest(
            unthreadLL(first_half),
            unthreadLL(reverse(second_half)),
        )))
                
        return threadLL(nodes)
        
        
