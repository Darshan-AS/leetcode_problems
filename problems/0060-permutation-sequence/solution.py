from sortedcontainers import SortedList

class Solution:
    factorials = list(accumulate(range(1, 10), operator.mul, initial=1))
    
    def getPermutation(self, n_: int, k: int) -> str:
        pool = SortedList(range(1, n_ + 1))
        permutation = []
        
        r = k - 1
        while pool:            
            q, r = divmod(r, self.factorials[len(pool) - 1])
            permutation.append(pool.pop(q))
        
        return ''.join(map(str, permutation))
