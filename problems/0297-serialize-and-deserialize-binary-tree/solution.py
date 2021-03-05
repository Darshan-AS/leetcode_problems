# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return f'{str(root.val)},{self.serialize(root.left)},{self.serialize(root.right)}' if root else str(None)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserialize_helper(datas):
            node = None if (x := datas.popleft()) is None else TreeNode(x)
            if not node: return node
            node.left = deserialize_helper(datas)
            node.right = deserialize_helper(datas)
            return node
        
        node_datas = deque(map(lambda s: int(s) if s != 'None' else None, data.split(',')))
        return deserialize_helper(node_datas)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
