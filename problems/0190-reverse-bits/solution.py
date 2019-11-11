class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i = n
        reverse_n = 0
        for _ in range(32):
            remainder = i % 2
            reverse_n = reverse_n * 2 + remainder
            i = i // 2
        
        return reverse_n
