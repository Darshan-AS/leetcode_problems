# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        def iter_LL(ll: ListNode | None) -> Iterable[ListNode]:
            node = ListNode(next=ll)
            while (node := node.next): yield node
        
        walker_nodes = iter_LL(head)
        runner_nodes = compress(iter_LL(head), cycle((0, 1)))
        return any(map(eq, walker_nodes, runner_nodes))

