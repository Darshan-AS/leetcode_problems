class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(list1), len(list2)
        
        def find_intersection(i1, i2):
            start = max(i1[0], i2[0])
            end = min(i1[1], i2[1])
            return [start, end] if start <= end else []
        
        while i < m and j < n:
            intersection = find_intersection(list1[i], list2[j])
            if intersection: yield intersection
            i, j = (i + 1, j) if list1[i][1] < list2[j][1] else (i, j + 1)
