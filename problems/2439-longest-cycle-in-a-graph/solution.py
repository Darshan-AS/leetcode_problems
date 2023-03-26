class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        def iter_edges(x):
            while x != -1: yield x; x = edges[x]
        
        visited = set()
        m = -1
        for u in range(len(edges)):
            if u in visited: continue
            seen = {}
            for i, x in enumerate(iter_edges(u)):
                if x in seen: m = max(m, i - seen[x]); break
                if x in visited: break
                seen[x] = i
                visited.add(x)
        return m

