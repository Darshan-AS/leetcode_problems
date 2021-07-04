import numpy as np


class Solution:
    dfa_matrix = np.array(
        [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0],
        ]
    )
    
    def countVowelPermutation(self, n: int) -> int:
        state = np.ones(5)
        for _ in range(n - 1):
            state = (self.dfa_matrix @ state) % 1_000_000_007
        return int(state.sum() % 1_000_000_007)

        
