from itertools import accumulate, chain
class Solution:
    def getRow(self, k: int) -> List[int]:        
        half_row = list(accumulate(
            range(1, (k // 2) + 1),
            lambda a, x: a * (k - (x - 1)) // x,
            initial=1,
        ))
                           
        return half_row + half_row[-1 if k % 2 else -2::-1]
