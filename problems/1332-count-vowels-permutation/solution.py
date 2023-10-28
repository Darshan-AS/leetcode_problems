import numpy as np

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1_000_000_007
        transitions = np.array([
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0],
        ])

        counts = reduce(lambda a, _: transitions @ a % M, range(1, n), np.ones(5))
        return int(counts.sum()) % M
