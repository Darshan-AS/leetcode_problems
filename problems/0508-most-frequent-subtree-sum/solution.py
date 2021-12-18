# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root_: Optional[TreeNode]) -> List[int]:
        def sub_tree_sums(root: Optional[TreeNode]) -> Iterator[int]:
            if not root: return
            
            ls = sub_tree_sums(root.left)
            rs = sub_tree_sums(root.right)
            
            l_sum, r_sum = next(ls, None), next(rs, None)
            yield root.val + (l_sum if l_sum else 0) + (r_sum if r_sum else 0)
            
            if l_sum is not None: yield from chain((l_sum,), ls)
            if r_sum is not None: yield from chain((r_sum,), rs)
        
        c = Counter(list(sub_tree_sums(root_)))
        max_count = max(c.values())
        return [k for k, v in c.items() if v == max_count]
            
            
