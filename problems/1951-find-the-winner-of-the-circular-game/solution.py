class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return reduce(lambda a, x: (a + k) % x, range(1, n + 1), 0) + 1
