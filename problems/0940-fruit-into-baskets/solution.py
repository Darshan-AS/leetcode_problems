class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def k_groupby(iterable: iter, k: int = 1):
            it = iter(iterable)
            queue = deque()
            counter = {}
            while (x := next(it, None)) is not None:
                if x not in counter and len(counter) == k:
                    yield queue
                    while len(counter) == k:
                        t = queue.popleft()
                        counter[t] -= 1
                        if not counter[t]: counter.pop(t)
                queue.append(x)
                counter[x] = counter.get(x, 0) + 1
            yield queue
        
        return max(sum(1 for _ in g) for g in k_groupby(fruits, 2))

