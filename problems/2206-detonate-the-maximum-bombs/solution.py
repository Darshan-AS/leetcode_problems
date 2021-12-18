class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dist = lambda p1, p2: math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        
        n = len(bombs)
        
        g = {
            i: [j for j in range(n) if i != j and dist(bombs[i][:-1], bombs[j][:-1]) <= bombs[i][-1]]
            for i in range(n)
        }
        
        def connections(root, seen=None):
            seen = set() if seen is None else seen
            seen.add(root)
            return 1 + sum(connections(node, seen) for node in g[root] if node not in seen)
        
        return max(map(connections, range(n)))
        
        
