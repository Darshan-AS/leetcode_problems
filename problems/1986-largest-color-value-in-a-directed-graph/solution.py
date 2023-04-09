class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        Node = int
        Color = str
        Graph = Mapping[Node, tuple[Color, Collection[Node]]]

        def max_color_count(graph: Graph) -> int:
            seen: set[Node] = set()
            sentinal = object()
            union_or_break = lambda c, node: c if sentinal in c else c | count_colors(node)

            @cache
            def count_colors(root: Node) -> Counter[Color]:
                color, nodes = graph[root]
                if root in seen: return Counter({sentinal: inf})

                seen.add(root)
                counter = Counter({color: 1}) + reduce(union_or_break, nodes, Counter())
                seen.remove(root)

                return counter
            
            return max(count_colors(node).most_common(1)[0][1] for node in graph)
        

        graph: Graph = {i: (c, set()) for i, c in enumerate(colors)}
        for u, v in edges: graph[u][1].add(v)

        count: int = max_color_count(graph)
        return -1 if count == inf else count
