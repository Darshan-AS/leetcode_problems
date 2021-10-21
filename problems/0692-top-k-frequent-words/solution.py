from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for word, _ in heapq.nsmallest(k, Counter(words).items(), key=lambda x: (-x[1], x[0]))]
        
