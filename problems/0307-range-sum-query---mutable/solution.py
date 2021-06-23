import operator
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


class SegmentTree:
    class Node:
        def __init__(self, value: T, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self, func: Callable[[T, T], T], seq: Sequence[T]):
        def make_segment(low: int, high: int):
            if low == high:
                return SegmentTree.Node(seq[low])

            mid = low + (high - low) // 2

            left_node = make_segment(low, mid)
            right_node = make_segment(mid + 1, high)

            return SegmentTree.Node(
                func(left_node.value, right_node.value),
                left_node,
                right_node,
            )

        self.func = func
        self.root = make_segment(0, len(seq) - 1)
        self.size = len(seq)

    def update(self, index: int, value: T) -> None:
        def update_segment(node: SegmentTree.Node, low: int, high: int):
            if low == high:
                node.value = value
                return

            mid = low + (high - low) // 2
            if index <= mid:
                update_segment(node.left, low, mid)
            elif index > mid:
                update_segment(node.right, mid + 1, high)

            node.value = self.func(node.left.value, node.right.value)

        update_segment(self.root, 0, self.size - 1)

    def query(self, left: int, right: int) -> int:
        def query_segment(node: SegmentTree.Node, low: int, high: int):
            if left <= low and right >= high:
                return node.value

            mid = low + (high - low) // 2

            if left > mid:
                return query_segment(node.right, mid + 1, high)
            elif right <= mid:
                return query_segment(node.left, low, mid)

            left_value = query_segment(node.left, low, mid)
            right_value = query_segment(node.right, mid + 1, high)

            return self.func(left_value, right_value)

        return query_segment(self.root, 0, self.size - 1)


class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(operator.add, nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
