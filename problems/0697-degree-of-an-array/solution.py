class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_count = defaultdict(lambda: (0, -1, -1)) # (count, first seen at index, last seen at index)
        
        for i, num in enumerate(nums):
            count, first_seen, _ = num_count[num]
            num_count[num] = (count + 1, first_seen if first_seen >= 0 else i, i)
        
        _, min_len = max((c, -(j - i + 1)) for c, i, j in num_count.values())
        return -min_len
