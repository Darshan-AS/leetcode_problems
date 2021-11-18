class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def min_distance(w1, w2):
            if not w1 or not w2: return max(len(w1), len(w2))
            
            return (
                min_distance(w1[1:], w2[1:])
                if w1[0] == w2[0] 
                else 1 + min(
                    min_distance(w1[1:], w2[1:]),
                    min_distance(w1, w2[1:]),
                    min_distance(w1[1:], w2),
                )
            )
        
        return min_distance(word1, word2)
