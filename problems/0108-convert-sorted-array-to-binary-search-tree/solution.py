# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def sorted_seq_to_BST(seq: Sequence, start: int, end: int) -> TreeNode | None:
            if start > end: return None
            
            mid = (start + end) // 2
            return TreeNode(
                seq[mid],
                sorted_seq_to_BST(seq, start, mid - 1),
                sorted_seq_to_BST(seq, mid + 1, end),
            )
        
        return sorted_seq_to_BST(nums, 0, len(nums) - 1)
