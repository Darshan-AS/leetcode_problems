class Solution:
    def trap(self, height: List[int]) -> int:
        water_units = 0
        
        i, j = 0, len(height) - 1
        max_h = 0
        while i < j:
            h = min(height[i], height[j])
            max_h = max(max_h, h)
            water_units += max_h - h
            i, j = (i + 1, j) if h == height[i] else (i, j - 1)
        
        return water_units
