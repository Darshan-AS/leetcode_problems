class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum((c := sum(1 for _ in g)) * (c + 1) // 2 for _, g in groupby(s)) % 1_000_000_007
        
