class Solution:
    def maxNiceDivisors(self, prime_factors: int) -> int:
        # Similar to 343. Integer break
        num = prime_factors
        if num <= 1: return 1
        
        M = 1_000_000_007
        q, r = divmod(num, 3)
        
        if r == 0:
            return pow(3, q, M)
        elif r == 1:
            return pow(3, q - 1, M) * 4 % M
        elif r == 2:
            return pow(3, q, M) * 2 % M
