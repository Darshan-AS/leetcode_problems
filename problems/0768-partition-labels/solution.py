class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {ch: i for i, ch in enumerate(s)}
        
        lengths = []
        i, j = -1, 0 # (i, j] is current partition
        
        for k, ch in enumerate(s):
            j = max(j, last_index[ch])
            if k == j:
                lengths.append(j - i)
                i = j
        
        return lengths
