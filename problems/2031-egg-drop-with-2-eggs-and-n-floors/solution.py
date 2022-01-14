class Solution:
    def twoEggDrop(self, n: int) -> int:
        # return x such that x + (x - 1) + (x - 2) + ... + 3 + 2 + 1 = n
        return ceil((-1 + sqrt(1 + 8 * n)) / 2)
