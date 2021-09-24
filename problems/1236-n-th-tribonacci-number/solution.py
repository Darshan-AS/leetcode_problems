class Solution:
    def tribonacci(self, n: int) -> int:
        fib_queue = collections.deque([0, 1, 1])
        for _ in range(3, n + 1):
            next_fib = sum(fib_queue)
            fib_queue.popleft()
            fib_queue.append(next_fib)
        return fib_queue[-1] if n >= 3 else fib_queue[n]
