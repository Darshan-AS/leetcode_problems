class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = list(accumulate(nums, operator.add, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
