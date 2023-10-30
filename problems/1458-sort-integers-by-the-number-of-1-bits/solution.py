class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def bit_count(n: int) -> int:
            bits = 0
            while n: bits += 1; n &= (n - 1)
            return bits
        
        return sorted(arr, key=lambda x: (bit_count(x), x))
        
