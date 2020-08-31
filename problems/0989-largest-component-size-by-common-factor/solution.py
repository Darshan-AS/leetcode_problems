from math import gcd
from itertools import takewhile, count
from collections import Counter

class DisjointSets:
    def __init__(self, n):
        self.sets = list(range(n))
    
    def find(self, x):
        if self.sets[x] != x:
            self.sets[x] = self.find(self.sets[x])
        return self.sets[x]
    
    def union(self, *x):
        head_set, *tail_sets = map(self.find, x)
        for s in tail_sets: self.sets[s] = head_set

def all_primes():    
    def sieve(seq):
        p = next(seq)
        yield p
        yield from sieve(filter(lambda x: x % p, seq))
    
    all_nums = count(2, 1)
    yield from sieve(all_nums)



class Solution:
    def primes_set(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:
        # primes = takewhile(lambda p: p <= max(A), all_primes())
        # factor_sets = filter(None, map(lambda p: [i for i, x in enumerate(A) if not x % p], primes))
        
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set: primes[q].append(i)
        factor_sets = primes.values()
        
        disjoin_sets = DisjointSets(len(A))
        for sets in factor_sets: disjoin_sets.union(*sets)
        return max(Counter(map(disjoin_sets.find, range(len(A)))).values())     
        
