# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
        
        prev, walker = walker, walker.next
        prev.next = None
        while walker:
            temp = walker.next
            walker.next = prev
            prev = walker
            walker = temp
        
        front, rear = head, prev
        curr_end = ListNode()
        while front and rear and front != rear:
            next_front = front.next
            next_rear = rear.next
            
            curr_end.next = front
            front.next = rear
            rear.next = None
            curr_end = rear
            
            front = next_front
            rear = next_rear
        
        if front == rear:
            curr_end.next = front
        
