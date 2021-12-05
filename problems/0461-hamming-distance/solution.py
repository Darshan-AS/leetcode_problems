class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def hamming_weight(n: int) -> int:
            count = 0
            while n:
                count += 1
                n &= (n - 1)
            return count
        
        return hamming_weight(x ^ y)
