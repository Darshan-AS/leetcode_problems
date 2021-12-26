class Solution:
    def numOfPairs(self, ss: List[str], target: str) -> int:
        s_counter = Counter(ss)
        
        return int(sum(
            ((s_counter[s] * s_counter[t]) if s != t else (s_counter[s] * (s_counter[s] - 1)))
            for s in s_counter
            for t in (target[len(s):],)
            if s == target[:len(s)]
        ))
