class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        return [w for w, _ in heapq.nsmallest(k, Counter(words).items(), key=lambda x: (-x[1], x[0]))]
