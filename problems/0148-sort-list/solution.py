# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Bottom up approach    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        n = self.length(head)
        split_size = 1
        head = ListNode(next=head)
        while split_size <= n:
            prev, curr = head, head.next
            while curr and curr.next:
                prev.next = None
                left, curr = self.split_first(curr, split_size)
                right, curr = self.split_first(curr, split_size)
                sorted_head, sorted_tail = self.merge(left, right)
                prev.next, sorted_tail.next = sorted_head, curr
                prev = sorted_tail
            split_size <<= 1
        return head.next
    
    def length(self, head: ListNode) -> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count
    
    def split_first(self, head: ListNode, size: int) -> (ListNode, ListNode):
        if not head: return head, head
        
        curr = prev = head
        while size and curr:
            prev = curr
            curr = curr.next
            size -= 1
        
        prev.next = None
        return head, curr
    
    def merge(self, left: ListNode, right: ListNode) -> (ListNode, ListNode):
        curr = head = ListNode()
        
        left_node, right_node = left, right
        while left_node and right_node:
            if left_node.val < right_node.val:
                curr.next = left_node
                left_node = left_node.next
            else:
                curr.next = right_node
                right_node = right_node.next
            curr = curr.next
        
        curr.next = left_node if left_node else right_node
        while curr and curr.next: curr = curr.next
        return head.next, curr
            
