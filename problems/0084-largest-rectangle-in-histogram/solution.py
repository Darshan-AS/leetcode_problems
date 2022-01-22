class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        
        heights.append(0)
        for j, h in enumerate(heights): # Append 0 to take care of non empty stack at the end
            while stack and heights[stack[-1]] > h:
                i = stack.pop()
                # Rectangle with ith bar as h = (left_len + right_len) * h = ((i - stack[i]) + (j - i) - 1) * h
                max_area = max(max_area, (j - stack[-1] - 1) * heights[i])
            stack.append(j)
        heights.pop()
        
        return max_area
