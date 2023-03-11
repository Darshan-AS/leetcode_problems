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
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        def iter_LL(ll: ListNode | None) -> Iterator[ListNode]:
            while ll: yield ll; ll = ll.next
        
        def len_LL(ll: ListNode | None) -> int:
            return sum(1 for _ in iter_LL(ll))
        
        def sorted_iter_to_BST(xs: Iterator, n: int) -> TreeNode | None:
            if n == 0: return None

            nl = (n - 1) // 2
            nr = (n - 1) - nl

            l_bst = sorted_iter_to_BST(xs, nl)
            val = next(xs)
            r_bst = sorted_iter_to_BST(xs, nr)

            return TreeNode(val, l_bst, r_bst)
        
        return sorted_iter_to_BST((x.val for x in iter_LL(head)), len_LL(head))

