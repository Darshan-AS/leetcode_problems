class Solution:
    def minCost(self, start_pos: List[int], home_pos: List[int], row_costs: List[int], col_costs: List[int]) -> int:
        x_low, x_high = (start_pos[0] + 1, home_pos[0] + 1) if start_pos[0] < home_pos[0] else (home_pos[0], start_pos[0])
        y_low, y_high = (start_pos[1] + 1, home_pos[1] + 1) if start_pos[1] < home_pos[1] else (home_pos[1], start_pos[1])
        
        return sum(row_costs[x_low: x_high]) + sum(col_costs[y_low: y_high])
