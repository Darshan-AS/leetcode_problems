# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd_head, even_head = head, head.next
        odd_ptr, even_ptr = odd_head, even_head
        
        while odd_ptr and even_ptr and odd_ptr.next and even_ptr.next:
            odd_ptr.next, even_ptr.next = odd_ptr.next.next, even_ptr.next.next
            odd_ptr, even_ptr = odd_ptr.next, even_ptr.next
            
        odd_ptr.next = even_head
        return odd_head
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
