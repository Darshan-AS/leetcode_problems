class Solution:
    def sortItems(self, n: int, m: int, group: list[int], before_items: list[list[int]]) -> list[int]:
        def toposort(deps):
            indegrees = {k: len(v) for k, v in deps.items()}

            zs_ = ((d, i) for i, ds in deps.items() for d in ds)
            zs = reduce(lambda a, x: a[x[0]].append(x[1]) or a, zs_, defaultdict(list))

            queue = deque((k for k, v in indegrees.items() if v == 0))
            ys = []
            while queue:
                pre = queue.popleft()
                ys.append(pre)
                
                for pt in zs[pre]:
                    indegrees[pt] -= 1
                    
                    if not indegrees[pt]:
                        queue.append(pt)
            
            return ys if len(ys) == len(deps) else []

            
        
        c = count(m)
        gs = [next(c) if g == -1 else g for g in group]
        xs = list((gs[i], gs[b]) for i, bs in enumerate(before_items) for b in bs if gs[i] != gs[b])
        d = reduce(lambda a, x: a[x[0]].append(x[1]) or a, xs, {i: [] for i in range(next(c))})

        ys = toposort(dict(enumerate(before_items)))
        zs = toposort(d)
        if not ys or not zs: return []

        dd = {z: [] for z in zs}
        for y in ys: dd[gs[y]].append(y)
        return [k for z in zs for k in dd[z]]
