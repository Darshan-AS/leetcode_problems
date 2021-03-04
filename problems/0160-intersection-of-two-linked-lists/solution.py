# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        pa_rotation = pb_rotation = 0
        
        while pa_rotation <= 1 and pb_rotation <= 1:
            if pa and pb and pa == pb: return pa   
            pa, pa_rotation = (pa.next, pa_rotation) if pa and pa.next else (headB, pa_rotation + 1)
            pb, pb_rotation = (pb.next, pb_rotation) if pb and pb.next else (headA, pb_rotation + 1)
                
            
