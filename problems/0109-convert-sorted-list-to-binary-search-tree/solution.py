# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head_: ListNode | None) -> TreeNode | None:
        def iter_LL(head: ListNode | None) -> Iterator:
            while head: yield head.val; head = head.next
        
        def len_LL(head: ListNode | None) -> int:
            return sum(1 for _ in iter_LL(head))
        
        def sorted_iterator_to_BST(values: Iterator, low: int, high: int) -> TreeNode | None:
            if low >= high: return None
            mid = (low + high) // 2
            
            left_bst  = sorted_iterator_to_BST(values, low, mid)
            root_val  = next(values)
            right_bst = sorted_iterator_to_BST(values, mid + 1, high)
            
            return TreeNode(root_val, left_bst, right_bst)
        
        return sorted_iterator_to_BST(iter_LL(head_), 0, len_LL(head_))
        
