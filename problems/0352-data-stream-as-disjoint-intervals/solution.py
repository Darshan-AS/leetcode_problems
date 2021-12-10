class SummaryRanges:

    def __init__(self):
        self.nodes = {}

    def addNum(self, v: int) -> None:
        if v in self.nodes: return
        
        self.nodes[v] = v
        self.union(v - 1, v)
        self.union(v, v + 1)

    def getIntervals(self) -> List[List[int]]:
        intervals = {}
        
        for u in self.nodes:
            v = self.root(u)
            intervals[v] = min(intervals[v], u) if v in intervals else u
        
        return sorted([[u, v] for v, u in intervals.items()])
    
    def union(self, u: int, v: int) -> None:
        if u not in self.nodes or v not in self.nodes: return
        
        ur = self.root(u)
        vr = self.root(v)
        
        self.nodes[ur] = vr
    
    def root(self, u: int) -> int:
        while self.nodes[u] != u:
            p = self.nodes[u]
            self.nodes[u] = self.nodes[p] # Path compression
            u = p
        return u


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
