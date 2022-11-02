class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        queue = deque([(start, 0)])
        bank = set(bank)
        
        while queue:
            node, steps = queue.popleft()
            if node == end: return steps
            
            adjs = {b for b in bank if sum(map(ne, node, b)) == 1}
            queue.extend((adj, steps + 1) for adj in adjs)
            bank -= adjs
        
        return -1
