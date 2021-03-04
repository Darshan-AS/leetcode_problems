# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return
        pa, pb = headA, headB
        a_crossed_end = b_crossed_end = False
        
        while True:
            if pa and pb and pa == pb: return pa
            
            if pa.next:
                pa = pa.next 
            else:
                if a_crossed_end: return
                pa = headB
                a_crossed_end = True
            
            if pb.next:
                pb = pb.next 
            else:
                if b_crossed_end: return
                pb = headA
                b_crossed_end = True
                
            
