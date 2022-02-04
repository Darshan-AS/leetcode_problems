# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    DELIMITER = ','

    def serialize(self, root: TreeNode | None) -> str:
        return ''.join((
            str(root.val),
            self.DELIMITER,
            self.serialize(root.left),
            self.DELIMITER,
            self.serialize(root.right),
        )) if root is not None else str(root)

    def deserialize(self, str_root: str) -> TreeNode | None:
        def preorder_build(values: Iterator[Any]) -> TreeNode | None:
            val = next(values)
            if val is None: return val
            
            root = TreeNode(val)
            root.left = preorder_build(values)
            root.right = preorder_build(values)
            return root
        
        vals = map(eval, str_root.split(self.DELIMITER))
        return preorder_build(vals)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
