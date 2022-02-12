class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.f_tree = FenwickTree(len(nums), nums)

    def update(self, index: int, val: int) -> None:
        self.f_tree.update(index, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.f_tree.range_query(left, right + 1)

class FenwickTree:
    def __init__(self, n, values=None):
        self.n = n
        self.tree = [0] * (n + 1)
        self.__treeify(values)

    def __treeify(self, values: Iterable) -> None:
        for i, value in enumerate(values, 1):
            self.tree[i] += value
            if (j := i + (i & -i)) <= self.n:
                self.tree[j] += self.tree[i]

    def range_query(self, start: int, end: int) -> Any:
        return self.query(end) - self.query(start)

    def query(self, end: int) -> Any:
        result = 0
        while end > 0:
            result += self.tree[end]
            end -= end & -end
        return result

    def update(self, index: int, value: int) -> None:
        index += 1
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
