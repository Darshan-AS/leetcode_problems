class Solution:
    def restoreArray(self, adjacent_pairs: list[list[int]]) -> list[int]:
        adjacents = defaultdict(set)
        for u, v in adjacent_pairs:
            adjacents[u].add(v)
            adjacents[v].add(u)

        def find_path(root: int, prev: int | None = None) -> list[int]:
            nexts = adjacents[root] - {prev}
            xs = find_path(nexts.pop(), root) if len(nexts) else []
            return xs.append(root) or xs
        
        ends = (x for x, nbrs in adjacents.items() if len(nbrs) == 1)
        return find_path(next(ends))
        
