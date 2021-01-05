# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        seen = set()
        _head = curr = ListNode(None, head)
        while curr and curr.next:
            seen.add(curr.val)
            if curr.next.val in seen:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return _head.next
