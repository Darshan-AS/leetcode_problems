# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        
        return pa
                
            
