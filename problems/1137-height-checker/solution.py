class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Counting sort
        counter = Counter(heights)
        
        expected = chain.from_iterable(map(
            lambda h: repeat(h, counter[h]),
            range(1, max(heights) + 1),
        ))
        
        return sum(map(operator.ne, expected, heights))
