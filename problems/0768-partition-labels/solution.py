from itertools import accumulate

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_map = {ch: i for i, ch in enumerate(s)}
        
        ans = []
        curr, prev_last = 0, -1
        for i, ch in enumerate(s):                
            curr = max(curr, last_map[ch])
            if i == curr:
                ans.append(curr - prev_last)
                prev_last = curr
        return ans
            
