class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def min_distance(i1: int, i2: int) -> int:
            if not i1 or not i2: return max(i1, i2)
            
            return (
                min_distance(i1 - 1, i2 - 1)
                if word1[i1 - 1] == word2[i2 - 1] 
                else 1 + min(
                    min_distance(i1 - 1, i2 - 1),
                    min_distance(i1, i2 - 1),
                    min_distance(i1 - 1, i2),
                )
            )
        
        return min_distance(len(word1), len(word2))
