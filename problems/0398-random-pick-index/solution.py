class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        candidates = (index for index, num in enumerate(self.nums) if num == target)
        
        winner = math.inf
        for i, c in enumerate(candidates):
            j = random.randint(0, i)
            if j == 0: winner = c
        
        return winner


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
