class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0
        for i in nums:
            if count == 0: candidate = i
            count += 1 if i == candidate else -1
        return candidate
