class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = list(accumulate(nums, operator.add))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right] - (self.prefix_sums[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
