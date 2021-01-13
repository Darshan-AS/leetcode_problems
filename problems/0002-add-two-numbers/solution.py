# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_head = ListNode()
        curr_l1, curr_l2, curr_sum = l1, l2, sum_head
        carry = 0
        while curr_l1 or curr_l2:
            curr_l1, l1_val = (curr_l1.next, curr_l1.val) if curr_l1 else (curr_l1, 0)
            curr_l2, l2_val = (curr_l2.next, curr_l2.val) if curr_l2 else (curr_l2, 0)
            carry, sum_ = divmod(l1_val + l2_val + carry, 10)
            curr_sum.next = ListNode(sum_)
            curr_sum = curr_sum.next
        curr_sum.next = ListNode(carry) if carry else curr_sum.next
        return sum_head.next
