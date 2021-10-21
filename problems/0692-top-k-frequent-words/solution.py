from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for word, _ in Counter(sorted(words)).most_common(k)]
