class Solution:
    def hammingWeight(self, n_: int) -> int:
        count = 0
        n = n_
        while n:
            count += 1
            n &= (n - 1)
        return count
