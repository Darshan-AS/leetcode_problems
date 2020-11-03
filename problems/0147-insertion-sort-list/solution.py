# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def sorted_insert(list_head, node):
            list_curr = list_head
            while list_curr and list_curr.next and list_curr.next.val <= node.val:
                list_curr = list_curr.next
            node.next = list_curr.next
            list_curr.next = node
            return list_head
        
        sol = ListNode()
        curr = head
        while curr:
            curr, sol = curr.next, sorted_insert(sol, curr)
        return sol.next
