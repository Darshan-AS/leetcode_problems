from sortedcontainers import SortedList

class Solution:
    factorials = list(accumulate(range(1, 10), operator.mul, initial=1))
    
    def getPermutation(self, n_: int, k_: int) -> str:
        def get_permutation(pool: list[int], k: int):            
            q, r = divmod(k, self.factorials[len(pool) - 1])
            
            yield pool.pop(q)
            yield from get_permutation(pool, r) if pool else ()
        
        # return ''.join(map(str, get_permutation(list(range(1, n_ + 1)), k_ - 1)))     # O(n ^ 2)
        return ''.join(map(str, get_permutation(SortedList(range(1, n_ + 1)), k_ - 1))) # O(n * log(n))

