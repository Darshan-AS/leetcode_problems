class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        stack = [-1]
        max_area = 0

        heights.append(0)
        for k in range(len(heights)):
            while heights[stack[-1]] > heights[k]:
                height = heights[stack.pop()]
                left, right = stack[-1], k
                
                # Rectangle with k-th bar as height
                curr_area = (right - left - 1) * height
                max_area = max(max_area, curr_area)

            stack.append(k)
        heights.pop()

        return max_area
