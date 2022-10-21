class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        
        for index, val in enumerate(nums):
            if val in seen and index - seen[val] <= k:
                return True
            seen[val] = index
        return False
