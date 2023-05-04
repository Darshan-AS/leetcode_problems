class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        
        rq, dq = reduce(
            lambda a, x: a[x[1] == 'D'].append(x[0]) or a,
            enumerate(senate),
            (deque(), deque()),
        )
        
        while rq and dq:
            r, d = rq.popleft(), dq.popleft()
            rq.append(r + n) if r < d else dq.append(d + n)
        
        return 'Radiant' if rq else 'Dire'
