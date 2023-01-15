class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        vals_to_nodes = defaultdict(list)
        for node, val in enumerate(vals): vals_to_nodes[val].append(node)

        graph = {x: [x] for x in range(len(vals))}
        for u, v in edges:
            low, high = (u, v) if vals[u] < vals[v] else (v, u)
            graph[high].append(low)
        
        dsu = DSU()
        paths = 0
        for val, nodes in sorted(vals_to_nodes.items()):
            for u in nodes:
                for v in graph[u]:
                    dsu.union(u, v)
            
            counts = Counter(map(dsu.find, nodes))
            paths += sum(map(lambda n: n * (n + 1) // 2, counts.values()))
        
        return paths



class DSU:
    T = Hashable

    def __init__(self, xs: Iterable[T] = tuple()) -> None:
        self.parents = {x: x for x in xs}
        self.sizes = {x: 1 for x in xs}
    
    def add(self, x: T) -> None:
        if x in self.parents: return
        self.parents[x] = x
        self.sizes[x] = 1
    
    def make_safe(func: Callable) -> Callable:
        """Decorator used to ensure input values are added to parents using in func"""
        def wrapper(self, *xs):
            for x in xs: self.add(x)
            return func(self, *xs)
        return wrapper
    
    @make_safe
    def union(self, u: T, v: T) -> None:
        ur, vr = self.find(u), self.find(v)
        short_t, long_t = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)

        self.parents[short_t] = long_t
        self.sizes[long_t] += self.sizes[short_t]
    
    @make_safe
    def find(self, x: T) -> T:
        self.parents[x] = self.find(self.parents[x]) if self.parents[x] != x else x
        return self.parents[x]
    
    @make_safe
    def is_connected(self, u: T, v: T) -> bool:
        return self.find(u) == self.find(v)
