class Solution:
    factorials = list(accumulate(range(1, 10), operator.mul, initial=1))
    
    def getPermutation(self, n_: int, k_: int) -> str:
        def get_permutation(pool: list[int], k: int):
            n = len(pool)
            
            if not k or n <= 1: return ''.join(map(str, pool))
            
            q, r = divmod(k, self.factorials[n - 1])
            q, r = (q, r) if r else (q - 1, self.factorials[n - 1])
            
            return str(pool[q]) + get_permutation(pool[:q] + pool[q + 1:], r)
        
        return get_permutation(list(range(1, n_ + 1)), k_)

