import bisect as b

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i, ch in enumerate(s) if ch == '|']
        plate_count = list(accumulate(s, lambda a, x: a + 1 if x == '*' else a, initial=0))[1:]
        
        counts = []
        for low, high in queries:
            li, hi = b.bisect_left(candles, low), b.bisect_right(candles, high) - 1
            if li >= len(candles) or hi < 0 or li >= hi:
                counts.append(0)
                continue
            
            counts.append(plate_count[candles[hi]] - plate_count[candles[li]])
        
        return counts
