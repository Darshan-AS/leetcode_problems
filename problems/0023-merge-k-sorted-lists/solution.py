# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ListNode.__lt__ = lambda self, other: self.val < other.val
ListNode.__eq__ = lambda self, other: self.val == other.val

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = curr = ListNode()
        pq = PriorityQueue()
        
        id = lambda x: x
        
        for l in filter(id, lists):
            pq.put((l.val, l))
        
        while not pq.empty():
            val, node = pq.get()
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node: pq.put((node.val, node))
        
        return dummy_head.next
