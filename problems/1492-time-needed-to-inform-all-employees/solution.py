class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager: list[int], inform_time: list[int]) -> int:
        Weight = int | float
        WeightedTree = tuple[Weight, Iterable['WeightedTree']]

        def max_path_sum(tree: WeightedTree) -> Weight:
            return tree[0] + max(map(max_path_sum, tree[1]), default=0)

        nodes = defaultdict(lambda: (0, []), {e: (t, []) for e, t in enumerate(inform_time)})
        for e, m in enumerate(manager): nodes[m][1].append(nodes[e])
        
        return max_path_sum(nodes[head_id])
