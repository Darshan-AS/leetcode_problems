# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        _head = curr = ListNode(None, head)
        value = curr.val
        while curr and (cn := curr.next):
            if cn.val == value or (cn.next and cn.val == cn.next.val):
                value = cn.val
                curr.next = cn.next
            else:
                curr = cn
        return _head.next
