class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        seen = defaultdict(int)
        
        for x in map(lambda n: n % k, arr):
            y = k - x if x else 0
            if seen[y]:
                seen[y] -= 1
            else:
                seen[x] += 1
        
        return all(c == 0 for c in seen.values())
