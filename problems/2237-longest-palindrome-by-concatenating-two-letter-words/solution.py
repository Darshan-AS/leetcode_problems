class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        seen = defaultdict(int)
        len_ = 0
        for w in words:
            v = w[1] + w[0]
            if seen[v] > 0:
                seen[v] -= 1
                len_ += 4
            else:
                seen[w] += 1
        
        has_center = any(w[0] == w[1] for w, c in seen.items() if c > 0)
        return len_ + (2 if has_center else 0)
            
