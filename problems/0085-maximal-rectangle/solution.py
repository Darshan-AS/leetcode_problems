class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Copied from Problem no: 84
        def largest_rectangle_area(heights: list[int]) -> int:
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
        
        histograms = list(accumulate(
            matrix,
            lambda hs, xs: list(map(lambda h, x: h + 1 if x == '1' else 0, hs, xs)),
            initial=[0] * len(matrix[0]),
        ))
                
        return max(map(largest_rectangle_area, histograms))
