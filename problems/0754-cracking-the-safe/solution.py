class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1: return ''.join(map(str, range(k)))
        
        def euler_cycle(g: dict, node: int) -> Iterator[int]:
            yield node[-1]
            while g[node]: yield from euler_cycle(g, g[node].pop())
        
        graph = defaultdict(list)
        for password in product(range(k), repeat=n):
            graph[password[:-1]].append(password[1:])
        
        start = (0,) * (n - 1)
        cycle = euler_cycle(graph, start)
        return ''.join(map(str, chain(start[:-1], cycle))) # Prepend missing n - 2 zeroes from the first password
