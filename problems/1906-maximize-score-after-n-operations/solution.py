class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs_score(mask: int) -> int:
            k = (n - mask.bit_count()) // 2
            return max((
                k * math.gcd(nums[i], nums[j]) + 
                dfs_score(mask | 1 << i | 1 << j) 
                for i in range(n) 
                for j in range(i + 1, n)
                if not mask & (1 << i | 1 << j)),
                default=0
            )
        
        return dfs_score(0)
