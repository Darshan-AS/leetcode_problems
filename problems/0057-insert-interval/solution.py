class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        
        def find_in_interval(intervals, x, is_left):
            start, end = 0, len(intervals) - 1
            
            while start <= end:
                mid = (start + end) // 2
                a, b = intervals[mid]
                
                if x < a: end = mid - 1
                elif x > b: start = mid + 1
                else: return mid
            
            return end if is_left else start
        
        left_index = find_in_interval(intervals, new_interval[0], False)
        right_index = find_in_interval(intervals, new_interval[1], True)
        
        result_interval = [
            min(intervals[left_index][0], new_interval[0]) if left_index < len(intervals) else new_interval[0],
            max(intervals[right_index][1], new_interval[1]) if right_index >= 0 else new_interval[1]
        ]
        
        return intervals[:left_index] + [result_interval] + intervals[right_index + 1:]
