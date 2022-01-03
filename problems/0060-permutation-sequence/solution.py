from sortedcontainers import SortedList

class Solution:
    factorials = list(accumulate(range(1, 10), operator.mul, initial=1))
    
    def getPermutation(self, n_: int, k_: int) -> str:
        def get_permutation(pool: list[int], k: int):
            n = len(pool)
            
            q, r = divmod(k, self.factorials[n - 1])
            q, r = (q, r) if r else (q - 1, self.factorials[n - 1])
            
            yield pool.pop(q)
            yield from get_permutation(pool, r) if r and len(pool) > 1 else pool
        
        # return ''.join(map(str, get_permutation(list(range(1, n_ + 1)), k_)))     # O(n ^ 2)
        return ''.join(map(str, get_permutation(SortedList(range(1, n_ + 1)), k_))) # O(n * log(n))

