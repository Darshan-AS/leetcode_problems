class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        
        # For k > 1, all permutations can be achieved, and hence we can do bubble sort
        return ''.join(sorted(s))
