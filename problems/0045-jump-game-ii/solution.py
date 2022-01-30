class Solution:
    def jump(self, nums: List[int]) -> int:
        i, j, n = 0, 0, len(nums)
        jumps = 0
        
        next_j = j
        while i <= j < n - 1:
            i, next_j = i + 1, max(next_j, i + nums[i])
            if i > j: j = next_j; jumps += 1
        
        return jumps if j >= n - 1 else -1
