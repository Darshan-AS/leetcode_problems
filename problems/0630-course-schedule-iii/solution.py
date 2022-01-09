class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        time_used = 0
        
        for duration, last_day in sorted(courses, key=lambda x: x[1]):
            if time_used + duration <= last_day:
                time_used += duration
                heappush(heap, -duration)
            elif heap and -heap[0] > duration:
                time_used += duration + heappop(heap)
                heappush(heap, -duration)
                    
        return len(heap)
