# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinal_head = c = ListNode(None, head)
        
        val = c.val
        while c and (cn := c.next):
            if cn.val == val or (cn.next and cn.val == cn.next.val):
                c.next = cn.next
                val = cn.val
            else:
                c = c.next
        
        return sentinal_head.next
