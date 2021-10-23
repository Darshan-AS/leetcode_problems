class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcds = sorted((
            (math.gcd(nums[i], nums[j]), 1 << i | 1 << j)
            for i in range(n)
            for j in range(i + 1, n)),
            reverse=True
        )
                
        def dfs_score(mask, k):
            max_score = 0
            if not k: return max_score
            for gcd, ij_mask in gcds:
                if (
                    not mask & ij_mask
                    and max_score < gcd * k * (k + 1) / 2 # Prune if max possible score on exploring the branch is not greater than current max_score
                ):
                    max_score = max(max_score, k * gcd + dfs_score(mask | ij_mask, k - 1))
            return max_score
        
        return dfs_score(0, n // 2)
