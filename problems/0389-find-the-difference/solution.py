from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return x.most_common(1)[0][0] if (x := (Counter(t) - Counter(s))) else list(set(b) - set(a))[0]
