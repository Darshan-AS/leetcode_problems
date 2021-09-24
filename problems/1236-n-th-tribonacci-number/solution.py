class Solution:
    def tribonacci(self, n: int) -> int:
        fib_queue = collections.deque([0, 1, 1], maxlen=3)
        for _ in range(3, n + 1):
            fib_queue.append(sum(fib_queue))
        return fib_queue[-1] if n >= 3 else fib_queue[n]
