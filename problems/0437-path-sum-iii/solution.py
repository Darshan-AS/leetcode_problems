# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root_: Optional[TreeNode], target_sum: int) -> int:
        def count_path_sum(root: Optional[TreeNode], curr_sum: int = 0, prefix_sums: dict = None) -> int:
            prefix_sums = defaultdict(int, {0: 1}) if prefix_sums is None else prefix_sums
            if not root: return 0
            
            next_sum = curr_sum + root.val
            
            prefix_sums[next_sum] += 1
            left_count  = count_path_sum(root.left , next_sum, prefix_sums)
            right_count = count_path_sum(root.right, next_sum, prefix_sums)
            prefix_sums[next_sum] -= 1
            
            return left_count + right_count + prefix_sums[next_sum - target_sum]
        
        return count_path_sum(root_)

