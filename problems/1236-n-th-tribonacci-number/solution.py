from itertools import islice
from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        def trib():
            trib_queue = deque([0, 1, 1], maxlen=3)
            sum_ = sum(trib_queue)
            while True:
                k = trib_queue.popleft()
                yield k
                trib_queue.append(sum_)
                sum_ = sum_ + sum_ - k
                
        return next(islice(trib(), n, None))
