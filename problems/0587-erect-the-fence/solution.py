from itertools import chain

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) < 4: return points
        
        orientation = lambda p, q, r: (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) 
        
        outer_trees_stack = []
        sorted_points = list(sorted(points))
        
        for point in sorted_points:
            while len(outer_trees_stack) >= 2 and \
                orientation(outer_trees_stack[-2], outer_trees_stack[-1], point) > 0:
                outer_trees_stack.pop()
            outer_trees_stack.append(point)
        
        outer_trees_stack.pop()
        
        for point in reversed(sorted_points):
            while len(outer_trees_stack) >= 2 and \
                orientation(outer_trees_stack[-2], outer_trees_stack[-1], point) > 0:
                outer_trees_stack.pop()
            outer_trees_stack.append(point)
        
        return set(map(tuple, outer_trees_stack))
                
        
