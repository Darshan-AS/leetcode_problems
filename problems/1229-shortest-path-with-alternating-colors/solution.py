class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: list[list[int]], blue_edges: list[list[int]]) -> list[int]:
        RED, BLUE = -1, +1
        flip = lambda color: -color # Flips color between RED and BLUE

        Color = RED | BLUE
        Node = int
        RedNodes  = dict[RED , list[Node]]
        BlueNodes = dict[BLUE, list[Node]]
        ColoredGraph = dict[Node, tuple[RedNodes, BlueNodes]]
        Distances = dict[Node, int]

        def shortest_dist(graph: ColoredGraph, src: Node) -> Distances:
            """Finds shortest dist from src to all other nodes"""
            queue = deque(((src, RED, 0), (src, BLUE, 0))) # (source node, previous edge color, distance)
            seen = {(src, RED), (src, BLUE)}
            dists = {i: inf for i in graph}; dists[0] = 0

            while queue:
                node, prev_color, dist = queue.popleft()
                next_color = flip(prev_color)

                for nbr in filter(lambda nbr: (nbr, next_color) not in seen, graph[node][next_color]):
                    queue.append((nbr, next_color, dist + 1))
                    seen.add((nbr, next_color))
                    dists[nbr] = min(dists[nbr], dist + 1)
            
            return dists
        
        g: ColoredGraph = {i: {RED: [], BLUE: []} for i in range(n)}
        for u, v in red_edges: g[u][RED].append(v)
        for u, v in blue_edges: g[u][BLUE].append(v)

        dists: Distances = shortest_dist(g, 0)
        return [-1 if dists[i] == inf else dists[i] for i in range(n)]

