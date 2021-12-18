class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        default_value = (0, 1) # (lts_length, lts_count)
        
        def merge(x, y):
            return (x[0], x[1] + y[1]) if x[0] == y[0] and x[0] != 0 else max(x, y)
 
        if not nums: return 0
        
        start, end = min(nums), max(nums)
        st = SegmentTree(start, end, default_value, merge)
        for num in nums:
            res = st.query(start, num - 1)
            st.insert(num, (res[0] + 1, res[1]))
        return st.root.value[1]
        

from typing import Callable, TypeVar

T = TypeVar("T")


class SegmentTree:
    class Node:
        def __init__(self, value: T, start: int, end: int, left=None, right=None):
            self.value = value
            self.start = start
            self.end = end
            self.left = left
            self.right = right

        @property
        def mid(self):
            return (self.start + self.end) // 2

    def __init__(
        self, start: int, end: int, default_value: T, func: Callable[[T, T], T]
    ):
        self.func = func
        self.default_value = default_value
        self.root = SegmentTree.Node(default_value, start, end)

    def safe_left(self, node: Node):
        node.left = (
            node.left
            if node.left
            else SegmentTree.Node(self.default_value, node.start, node.mid)
        )
        return node.left

    def safe_right(self, node: Node):
        node.right = (
            node.right
            if node.right
            else SegmentTree.Node(self.default_value, node.mid + 1, node.end)
        )
        return node.right

    def insert(self, key: int, value: T) -> None:
        def insert_segment(node: SegmentTree.Node):
            if node.start == node.end:
                node.value = self.func(value, node.value)
                return

            if key <= node.mid:
                insert_segment(self.safe_left(node))
            elif key > node.mid:
                insert_segment(self.safe_right(node))

            node.value = self.func(
                self.safe_left(node).value, self.safe_right(node).value
            )

        insert_segment(self.root)

    def update(self, key: int, value: T) -> None:
        self.insert(key, value)

    def query(self, start: int, end: int) -> int:
        def query_segment(node: SegmentTree.Node):
            if start <= node.start <= node.end <= end:
                return node.value

            if end < start or end < node.start or node.end < start:
                return self.default_value

            left_value = query_segment(self.safe_left(node))
            right_value = query_segment(self.safe_right(node))

            return self.func(left_value, right_value)

        return query_segment(self.root)
