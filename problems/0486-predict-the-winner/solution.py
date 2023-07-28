class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        @cache
        def score(i: int, j: int) -> int:
            return (i <= j) and max(
                nums[i] - score(i + 1, j),
                nums[j] - score(i, j - 1),
            )
        
        return len(nums) % 2 == 0 or score(0, len(nums) - 1) >= 0
