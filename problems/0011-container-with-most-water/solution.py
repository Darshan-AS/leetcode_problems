class Solution:
    def maxArea(self, h: List[int]) -> int:
        i, j = 0, len(h) - 1
        
        max_area = 0
        while i < j:
            max_area = max(max_area, min(h[i], h[j]) * (j - i))
            i, j = (i + 1, j) if h[i] < h[j] else (i, j - 1)
        
        return max_area
