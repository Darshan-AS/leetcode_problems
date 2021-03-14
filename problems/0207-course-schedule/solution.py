from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        
        for course, pre_course in prerequisites:
            graph[pre_course].add(course)
            indegrees[course] += 1
        
        course_selected_count = 0
        queue = deque((course for course in range(numCourses) if not indegrees[course]))
        while queue:
            pre_course = queue.popleft()
            course_selected_count += 1
            
            for course in graph[pre_course]:
                indegrees[course] -= 1
                
                if not indegrees[course]:
                    queue.append(course)
        
        return course_selected_count == numCourses
