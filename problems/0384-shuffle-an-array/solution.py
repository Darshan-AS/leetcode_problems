class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return list(self.nums)

    def shuffle(self) -> List[int]:
        nums = list(self.nums)
        for i in range(len(self.nums)):
            j = random.randrange(i + 1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
