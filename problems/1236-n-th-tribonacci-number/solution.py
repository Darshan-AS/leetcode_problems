from collections.abc import *
from numbers import Number

class Solution:
    def tribonacci(self, n: int) -> int:
        T = Number
        def kibonaccis(inits: Iterable[T], k: int) -> Iterable[T]:
            assert k >= 1, "k should be atleast 1"
            dq = deque(islice(inits, k), k)
            assert len(dq) == k, "Length of inits should be >= k"

            rt = sum(dq)
            while True:
                lt = dq.popleft()
                dq.append(rt)
                rt += rt - lt
                yield lt
        
        return next(islice(kibonaccis((0, 1, 1), 3), n, None))
