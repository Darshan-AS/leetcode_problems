class Solution:
    def reverseBits(self, n: int) -> int:
        i = n
        reverse_n = 0
        for _ in range(32):
            reverse_n = (reverse_n << 1) + (i & 1)
            i >>= 1
        
        return reverse_n
