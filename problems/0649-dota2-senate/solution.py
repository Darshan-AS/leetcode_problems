class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rc = senate.count('R')
        dc = len(senate) - rc
        c = 0

        q = deque(senate)
        while rc and dc:
            s = q.popleft()
            if s == 'R' and c >= 0: q.append(s)
            if s == 'R' and c <  0: rc -= 1
            if s == 'D' and c <= 0: q.append(s)
            if s == 'D' and c >  0: dc -= 1
            c += 1 if s == 'R' else -1
        
        return 'Radiant' if rc else 'Dire'
