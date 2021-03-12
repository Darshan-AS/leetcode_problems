# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

ListNode.__lt__ = lambda self, x: self.val < x.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        p_queue = PriorityQueue()
        merged_head = merged_curr = ListNode()
        
        for head_node in filter(None, lists):
            p_queue.put((head_node.val, head_node))
        
        while not p_queue.empty():
            _, node = p_queue.get()
            if node.next:
                p_queue.put((node.next.val, node.next))
            
            merged_curr.next = node
            merged_curr = merged_curr.next
        
        return merged_head.next
