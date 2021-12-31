class Solution:
    def numTrees(self, n: int) -> int:
        # nth Catalan number
        return round(reduce(operator.mul, map(lambda k: (n + k) / k, range(2, n + 1)), 1))
