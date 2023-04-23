class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache
        def count_arrays(i: int) -> int:
            if i == len(s): return 1
            if s[i] == '0': return 0
            js = takewhile(lambda j: int(s[i : j]) <= k, range(i + 1, len(s) + 1))
            return sum(map(count_arrays, js)) % 1_000_000_007
        
        return count_arrays(0)
