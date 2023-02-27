"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        def build_quad(i1: int, j1: int, i2: int, j2: int) -> 'Node':
            if (i1, j1) == (i2, j2): return Node(grid[i1][j1], True)

            im, jm = i1 + (i2 - i1) // 2, j1 + (j2 - j1) // 2
            tl = build_quad(i1, j1, im, jm)
            tr = build_quad(i1, jm + 1, im, j2)
            bl = build_quad(im + 1, j1, i2, jm)
            br = build_quad(im + 1, jm + 1, i2, j2)

            sub_trees = (tl, tr, bl, br)
            val_ = tl.val
            are_leaves = all(node.isLeaf == True for node in sub_trees)
            are_same_val = all(node.val == val_ for node in sub_trees)

            return Node(val_, True) if are_leaves and are_same_val else Node(val_, False, tl, tr, bl, br)

        m, n = len(grid), len(grid[0])
        return build_quad(0, 0, m - 1, n - 1)
