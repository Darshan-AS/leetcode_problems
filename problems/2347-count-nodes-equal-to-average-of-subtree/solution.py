# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def count_avg(root: TreeNode | None) -> int:
            if root is None: return 0, 0, 0

            l_cnt, l_sum, l_len, = count_avg(root.left)
            r_cnt, r_sum, r_len = count_avg(root.right)

            sum_ = l_sum + r_sum + root.val
            len_ = l_len + r_len + 1
            cnt_ = l_cnt + r_cnt + (sum_ // len_ == root.val)

            return cnt_, sum_, len_
        
        return count_avg(root)[0]
        
