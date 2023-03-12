# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        ListNode.__lt__ = lambda self, x: self.val < x.val

        merged_head = merged_tail = ListNode()
        hq = [ll for ll in lists if ll is not None]
        heapify(hq)

        while hq:
            node = heappop(hq)
            if node.next: heappush(hq, node.next)
            
            merged_tail.next = ListNode(node.val)
            merged_tail = merged_tail.next
        
        return merged_head.next


