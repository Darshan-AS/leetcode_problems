class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)
        gcds = sorted((
            (gcd(nums[i], nums[j]), 1 << i | 1 << j)
            for i in range(n)
            for j in range(i + 1, n)),
            reverse=True,
        )

        
        def score(xs: list[int], mask: int=0) -> int:
            n = len(xs)
            k = (n - mask.bit_count()) // 2

            max_score = 0
            for gcd_, ij_mask in gcds:
                if (not (mask & ij_mask)                        # Prune if the gcd pair is already used.
                    and max_score < gcd_ * (k * (k + 1) // 2)   # Prune if max possible score on exploring the branch is not greater than current max_score
                ): max_score = max(max_score, k * gcd_ + score(xs, mask | ij_mask))
            
            return max_score
        
        return score(nums)
