class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n, score = len(nums), list(nums)
        any(
            setitem(score, l, max(nums[l] - score[l + 1], nums[r] - score[l]))
            for d in range(1, n) for l in range(n - d) for r in (l + d,)
        )
        return score[0] >= 0
