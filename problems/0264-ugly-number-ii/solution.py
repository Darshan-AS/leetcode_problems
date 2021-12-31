class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def ugly_numbers():
            u = 1
            yield u
            q2, q3, q5 = deque([2]), deque([3]), deque([5])
            while True:
                q = min(q2, q3, q5)
                x = q.popleft()
                yield x
                
                if q is q2:
                    q2.append(x * 2); q3.append(x * 3); q5.append(x * 5)
                elif q is q3:
                    q3.append(x * 3); q5.append(x * 5)
                elif q is q5:
                    q5.append(x * 5)
        
        return next(islice(ugly_numbers(), n - 1, None))
