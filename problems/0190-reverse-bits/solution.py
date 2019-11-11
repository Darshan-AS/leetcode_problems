class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i = n
        reverse_n = 0
        for _ in range(32):
            reverse_n = (reverse_n << 1) + (i & 1)
            i >>= 1
        
        return reverse_n
