# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        def iter_LL(ll: ListNode | None) -> Iterable[ListNode]:
            node = ListNode(next=ll)
            while (node := node.next): yield node
        
        walker_nodes = iter_LL(head)
        runner_nodes = compress(iter_LL(head), cycle((0, 1)))
        
        meet = next((w.next for w, r in zip(walker_nodes, runner_nodes) if w == r), None)
        return next((a for a, b in zip(iter_LL(head), iter_LL(meet)) if a == b), None)
