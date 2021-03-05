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
        def bfs(root_):
            level = (root_,)
            while level:
                yield from ((node.val if node else None) for node in level)
                level = tuple(child for node in level for child in ([node.left, node.right] if node else []))
        
        return ','.join(map(str, bfs(root)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_datas = deque(map(lambda s: int(s) if s != 'None' else None, data.split(',')))
        getNextTreeNode = lambda datas: None if (x := node_datas.popleft()) is None else TreeNode(x)
        
        root = getNextTreeNode(node_datas)
        if not root: return
        
        queue = deque((root,))
        while queue:
            node = queue.popleft()
            node.left = getNextTreeNode(node_datas)
            node.right = getNextTreeNode(node_datas)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
