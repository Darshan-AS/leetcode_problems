from itertools import accumulate, chain
class Solution:
    def getRow(self, k: int) -> List[int]:
        k_mid = (k + 1) // 2 if k % 2 else (k // 2) + 1
        
        iterator = chain([1], range(1, k_mid))
        get_next_value = lambda prev_value, x: prev_value * (k - x + 1) // x
        half_answer = list(accumulate(iterator, get_next_value))
                           
        return half_answer + half_answer[-1 if k % 2 else -2::-1]
