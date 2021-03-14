from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        
        for course, pre_course in prerequisites:
            graph[pre_course].add(course)
            indegrees[course] += 1
        
        course_order = []
        queue = deque((course for course in range(numCourses) if not indegrees[course]))
        while queue:
            pre_course = queue.popleft()
            course_order.append(pre_course)
            
            for course in graph[pre_course]:
                indegrees[course] -= 1
                
                if not indegrees[course]:
                    queue.append(course)
        
        return course_order if len(course_order) == numCourses else []
