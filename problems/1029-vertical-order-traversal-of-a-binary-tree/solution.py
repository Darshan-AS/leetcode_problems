# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root_: Optional[TreeNode]) -> List[List[int]]:
        def vertical_traversal(
            root: Optional[TreeNode],
            row: int = 0,
            column: int = 0,
            col_row_map: Optional[dict[int, dict]] = None
        ) -> dict[int, dict]:
            col_row_map = defaultdict(lambda: defaultdict(list)) if col_row_map is None else col_row_map
            if not root: return col_row_map
            
            col_row_map[column][row].append(root.val)
            vertical_traversal(root.left , row + 1, column - 1, col_row_map)
            vertical_traversal(root.right, row + 1, column + 1, col_row_map)
            
            return col_row_map
        
        col_row_map = vertical_traversal(root_)
        return [
            list(chain.from_iterable(
                sorted(vals)
                for row, vals in sorted(row_map.items())
            ))
            for col, row_map in sorted(col_row_map.items())
        ]
        
        
            
