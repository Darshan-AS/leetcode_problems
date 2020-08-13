class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i
        return len(citations)
