class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:        
        n = len(bombs)
        
        g = {
            i: [
                j
                for j, (x2, y2, _) in enumerate(bombs)
                if i != j and (y2 - y1) ** 2 + (x2 - x1) ** 2 <= r1 ** 2
            ]
            for i, (x1, y1, r1) in enumerate(bombs)
        }
        
        def connections(root, seen=None):
            seen = set() if seen is None else seen
            seen.add(root)
            return 1 + sum(connections(node, seen) for node in g[root] if node not in seen)
        
        return max(map(connections, range(n)))
        
        
