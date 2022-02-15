class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        def euler_path(g: dict, node) -> Iterator:
            while g[node]: yield from euler_path(g, g[node].pop())
            yield node
        
        graph = defaultdict(list)
        for from_city, to_city in sorted(tickets, reverse=True):
            graph[from_city].append(to_city)
        
        return list(euler_path(graph, "JFK"))[::-1]
