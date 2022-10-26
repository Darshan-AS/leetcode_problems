class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        reminders = accumulate(nums, lambda a, x: (a + x) % k, initial=0)
        
        rem_idx = {}
        for i, r in enumerate(reminders):
            if r not in rem_idx: rem_idx[r] = i
            elif rem_idx[r] < i - 1: return True
        return False
