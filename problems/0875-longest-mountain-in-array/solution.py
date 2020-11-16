class Solution:
    def longestMountain(self, A: List[int]) -> int:
        def rise_count(arr):
            counts = [0]
            prev = -1
            for curr in arr:
                counts.append(counts[-1] + 1 if curr > prev else 1)
                prev = curr
            return counts[1:]
                    
        length = max(map(sum, filter(lambda x: x[0] > 1 and x[1] > 1, zip(rise_count(A), reversed(rise_count(reversed(A)))))), default=1) - 1
        return length if length >= 3 else 0
