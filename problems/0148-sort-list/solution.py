# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        left, right = self.split(head)
        sorted_left, sorted_right = self.sortList(left), self.sortList(right)
        return self.merge(sorted_left, sorted_right)
    
    def split(self, head: ListNode) -> (ListNode, ListNode):
        prev = walker = runner = head
        while runner and runner.next:
            prev = walker
            walker = walker.next
            runner = runner.next.next
        
        prev.next = None
        return head, walker
    
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
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
        return head.next
            
